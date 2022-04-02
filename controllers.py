import sys
import models
import views

from utils.helper import FormChecker
from utils.texts import Texts, TextsRanking, TextsForms

"""NB_PLAYERS sets the number of players per tournament.
NB_ROUNDS sets the number of rounds per tournament."""
NB_PLAYERS = 8
NB_ROUNDS = 4

class Control:
    def process_answer(self, answer, previous_view=None,
                    actions=None, return_home=False):
        """
        Processes a user answer to execute the corresponding function.
        """
        answer = answer.lower()

        if actions:
            for key in actions:
                if answer == key:
                    actions[key]()

        if answer == "q":
            sys.exit()

        if previous_view and answer == "r":
            if return_home == False:
                previous_view()
            else:
                app = MainControl()
                app.main()


class FormControl:
    def check_field(self, answer, validator=None,
                    error_message=TextsForms.not_blank):
        """
        Pass user answer through chosen validator function.
        """
        if len(answer) == 0:
            print(error_message)
            return False

        if validator:
            answer = validator(answer)
            if answer == False:
                print(error_message)

        return answer


    def check_list(self, answer, dict_content, error_message=""):
        """
        Check whether the answer is in dict_content.
        """
        if answer.strip() in dict_content.keys():
            return True

        else:
            print(error_message)
            return False


    def return_tournament_field(self, prompt, field_type, optional=False,
                                dict_content=None):
        return self.return_field(prompt, field_type, previous_view=True,
                                return_home=True, optional=optional,
                                dict_content=dict_content)


    def return_field(self, prompt, field_type, previous_view=None,
                        return_home=False, dict_content=None, optional=False):
        is_right = False

        while is_right == False:
            answer = self.menu.free_input(prompt).strip()
            self.process_answer(answer, previous_view=previous_view,
                        return_home=return_home)

            if optional == True and len(answer) == 0:
                return ""

            if field_type == "string":
                is_right = self.check_field(answer,
                                    error_message=TextsForms.not_blank)

            if field_type == "number":
                is_right = self.check_field(answer,
                                    validator=FormChecker.is_number,
                                    error_message=TextsForms.checker_number)

            if field_type == "previous_date":
                is_right = self.check_field(answer,
                                    validator=FormChecker.is_previous_date,
                                    error_message=TextsForms.checker_prev_date)

            if field_type == "later_date":
                is_right = self.check_field(answer,
                                    validator=FormChecker.is_later_date,
                                    error_message=TextsForms.checker_later_date)

            if field_type == "is_choice":
                is_right = self.check_field(answer)
                is_right = self.check_list(answer,
                                        dict_content=dict_content,
                                        error_message=TextsForms.checker_list)

        if field_type == "is_choice":
            return dict_content[answer]
        else:
            return answer

class MainControl(Control):
    def __init__(self):
        self.players = PlayerControl()
        self.rankings = RankingControl()
        self.tournament_menu = views.TournamentMenu()
        self.tournaments = TournamentControl()


    def main(self):
        answers=["n", "c", "r", "u"]
        answers_values=[self.create_tournament,
                self.ongoing_tournament,
                self.rankings.main,
                self.players.change_rank]
        actions_dict = dict(zip(answers, answers_values))
        menu = views.InputMenu(interrupts=["q"])
        answer = menu.ask_input(right_answers=answers,
                                prompt=Texts.main_menu,
                                )

        self.process_answer(answer, actions=actions_dict)


    def create_tournament(self):
        self.tournaments.create()
        self.tournaments.add_participants()
        self.tournaments.run()


    def ongoing_tournament(self):
        """
        If there are no ongoing tournament, launch create_tournament.
        If there is one, but lacking participants, launches add_participants,
        so we can create a tournament instance and add players at our own pace.
        Else, run the tournament.
        """
        tournament = models.Tournament.return_ongoing_tournament()

        if tournament == False:
            self.tournaments.create(from_c=True)

        elif len(models.Player.list_participants()) < NB_PLAYERS:
            self.tournaments.add_participants()
            self.tournaments.run()

        else:
            self.tournaments.run()


class TournamentControl(Control, FormControl):
    def __init__(self):
        self.menu = views.TournamentMenu()
        self.participants = PlayerControl()


    def add_participants(self):
        tournament = models.Tournament.return_ongoing_tournament()

        while len(models.Player.list_participants()) < NB_PLAYERS:
            self.players.main()

        for player_dict in models.Player.list_participants():
            player = models.Player(player_dict)
            tournament.players.append(player)

        tournament.save()


    def create(self, from_c=False):
        tournament_dict = {
            "name": self.return_tournament_field(TextsForms.tourn_name, "string"
                                                ),
            "place": self.return_tournament_field(TextsForms.tourn_place, "string"
                                                ),
            "date": self.return_tournament_field(TextsForms.tourn_date, "later_date"
                                                ),
            "duration": self.return_tournament_field(TextsForms.tourn_duration, "number"
                                                ),
            "time_control": self.return_tournament_field(TextsForms.time_control,
                                                "is_choice",
                                                dict_content=TextsForms.time_control_dict
                                                ),
            "description": self.return_tournament_field(TextsForms.tourn_desc,
                                                "string",
                                                optional=True
                                                ),
            "nb_rounds": NB_ROUNDS,
            "rounds": [],
            "players": [],
            "ended": "no",
            }

        tournament = models.Tournament(tournament_dict)
        turnament.save()

    def run(self):
        current_tournament = models.Tournament.return_last_tournament()
        while len(current_tournament.rounds) < NB_ROUNDS:
            TournamentControl.round_control()
            current_tournament = models.Tournament.return_last_tournament()

        current_tournament.set_ended()
        models.Player.clear_participants()

        list_tournament = models.Tournament.all_tournaments()
        finished_tournament = list_tournament[-1]
        rankings = models.Player.sort_list(finished_tournament["players"],
                                            score=True)
        answer = self.menu.end_screen(finished_tournament, rankings)
        self.process_answer(answer, previous_view=True, return_home=True)

    @staticmethod
    def round_control():
        tournament_instance = models.Tournament.return_last_tournament()
        tournament_instance.round_start()
        outcome = views.TournamentMenu.tournament_round(tournament_instance)
        if outcome == "q":
            sys.exit()
        else:
            tournament_instance.round_end(outcome)


class PlayerControl(Control):
    def __init__(self):
        self.menu = views.PlayerMenu()

    def main(self):
        condition = False
        while condition is False:
            answer = views.PlayerMenu.main()
            if answer == "1":
                if len(models.Player.list_not_participants()) == 0:
                    condition = True
                    print("Aucun joueur disponible : veuillez en créer.\n")
                    PlayerControl.create_player()
                else:
                    condition = True
                    PlayerControl.select_players()
            elif answer == "2":
                condition = True
                PlayerControl.create_player()
            elif choice == "q":
                sys.exit()

    def change_rank(self):
        """
        Takes a player index, checks the user doesn't want to cancel with
        process_answer, then does the same with the new point amount.
        """
        confirmed = False
        players = models.Player.all()
        self.menu.display_players_ranked(
                        "CHANGER LE CLASSEMENT D'UN JOUEUR\n",
                        players
                        )

        while confirmed == False:
            player = str(self.menu.ask_input(max_range=len(players),
                                                prompt=Texts.select_players)
                        )
            self.process_answer(player, previous_view=True, return_home=True)

            new_rank = str(self.menu.ask_input(max_range=10000,
                                                prompt=Texts.new_rank,
                                                is_float=True)
                        )
            self.process_answer(new_rank, previous_view=True, return_home=True)
            confirmed = self.menu.confirm_choice()

        picked = models.Player(players[int(player)-1])
        picked.change_rank(float(new_rank))

    def create_player():
        form = views.PlayerMenu.create_player()
        if form == "r":
            views.PlayerMenu.main()
        elif form == "q":
            sys.exit
        else:
            if FormChecker.check_date(form[2]) is False:
                print("Champs date de naissance :")
                new_date = FormChecker.correct_date(form[2])
                form[2] = new_date
            if FormChecker.check_gender(form[3]) is False:
                print("Champs genre :")
                form[3] = FormChecker.check_gender(form[3])
            if FormChecker.check_number(form[4]) is False:
                print("Champs classement :")
                form[4] = FormChecker.check_number(form[4])

            new_player = models.Player(
                {
                    "first_name": form[0],
                    "last_name": form[1],
                    "birth_date": form[2],
                    "gender": form[3],
                    "rank": int(form[4]),
                    "score": 0,
                    "is_playing": "False",
                }
            )
            if new_player.has_double() is True:
                print("Ce joueur existe déjà.\n")
                views.PlayerMenu.main()
            else:
                new_player.table_insert_player()
                print("Le joueur a été créé avec succès.\n")
                PlayerControl.main()

    def select_players():
        is_on = True
        while is_on and len(models.Player.list_participants()) < NB_PLAYERS:
            selection = views.PlayerMenu.select_players(
                models.Player.list_not_participants(),
                models.Player.list_participants(),
            )
            if selection == "q":
                sys.exit()
            elif selection == "r":
                print("Menu quitté.\n")
                is_on = False
                PlayerControl.main()
            else:
                selection = models.Player(selection)
                selection.is_playing_true()


class RankingControl(Control):
    def __init__(self):
        self.menu = views.Rankings()


    def main(self):
        answers = ["1", "2"]
        answers_values = [self.players, self.tournaments_list]
        actions_dict = dict(zip(answers, answers_values))
        answer = self.menu.ask_input(right_answers=answers,
                                prompt=TextsRanking.main)

        self.process_answer(answer,
                    actions=actions_dict,
                    previous_view=self.main,
                    return_home=True
                    )


    def players(self):
        #todo : adapt for tournaments
        """
        Opens a menu to display a player list sorted by name (a) or
        ranking (s).
        """
        players = models.Player.all()
        answers = ["a", "s"]

        answer = self.menu.ask_input(right_answers=answers,
                                prompt=TextsRanking.players).lower()

        if answer in answers:
            answer = self.display_players_list(answer, players)

        self.process_answer(answer, previous_view=self.main)


    def display_players_list(self, answer, players):
        """
        We lower() answer because this function is recursive and needs to
        format answers to itself. As long as Q or R aren't pressed, the function
        remains active.

        As process_answer doesn't take class methods with arguments, we use
        this setup for the alphabetical/ranking order switch.
        """
        answer = answer.lower()

        if answer == "a":
            list_alpha = models.Player.sort_list(players, alpha=True)
            answer = self.menu.players_sorted(
                                "JOUEURS PAR ORDRE ALPHABETIQUE\n",
                                list_alpha)
        elif answer == "s":
            list_ranked = models.Player.sort_list(players, rank=True)
            answer = self.menu.players_sorted(
                                "JOUEURS PAR SCORE\n",
                                list_ranked)

        elif answer in ["r", "q"]:
            self.process_answer(answer, previous_view=self.main)

        self.display_players_list(answer, players)


    def tournaments_list(self):
        list_tournaments = models.Tournament.all_tournaments()
        answer = self.menu.tournaments_list(list_tournaments)

        if str(answer).lower() not in ["r", "q"]:
            self.tournament(list_tournaments[answer - 1])
        else:
            self.process_answer(answer, previous_view=self.main)


    def tournament(self, tournament):
        """
        Shows explanations, then calls recursive display_tournament_detail
        to deal with user inputs.
        """
        players = models.Player.all()
        answers = ["a", "s", "d"]

        answer = self.menu.ask_input(right_answers=answers,
                                prompt=TextsRanking.tournament).lower()

        if answer in answers:
            answer = self.display_tournament_detail(tournament, answer)

        self.process_answer(answer, previous_view=self.tournaments_list)


    def display_tournament_detail(self, tournament, answer):
        """
        We lower() answer because this function is recursive and needs to
        format answers to itself. As long as Q or R aren't pressed, the function
        remains active.

        As process_answer doesn't take class methods with arguments, we use
        this setup.
        """
        #TODO: tournament argument?
        answer = answer.lower()
        players = tournament["players"]

        if answer == "a":
            list_alpha = models.Player.sort_list(players, alpha=True)
            answer = self.menu.players_sorted(
                                "JOUEURS PAR ORDRE ALPHABETIQUE\n",
                                list_alpha)

        elif answer == "s":
            list_ranked = models.Player.sort_list(players, score=True)
            answer = self.menu.players_sorted(
                                "JOUEURS PAR SCORE\n",
                                list_ranked)

        elif answer == "d":
            answer = self.menu.rounds(tournament)

        elif answer in ["r", "q"]:
            self.process_answer(answer, previous_view=self.tournaments_list)

        self.display_tournament_detail(tournament, answer)


class LanguageControl(Control):
    def valid_name(input):
        valid_name = ["english", "français", "francais"]
