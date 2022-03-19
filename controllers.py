import sys

import models
import views

from helper import CheckForm

"""NB_PLAYERS sets the number of players per tournament.
NB_ROUNDS sets the number of rounds per tournament."""
NB_PLAYERS = 8
NB_ROUNDS = 4


class TournamentControl:
    def __init__(self):
        self.tournament_menu = views.TournamentMenu()
        self.tournament_model = models.Tournament()

    def create_tournament():
        models.Player.clear_participants()
        form = views.TournamentMenu.create_tournament()
        if form == "q":
            sys.exit()
        elif form == "r":
            MainControl.main()
        else:
            if CheckForm.check_date(form[2]) is False:
                print("Erreur sur la date du tournoi.")
                new_date = CheckForm.correct_date(form[2])
                form[2] = new_date
            if CheckForm.check_number(form[3]) is False:
                print("Merci d'entrer un chiffre pour la durée du tournoi.")
                form[3] == CheckForm.check_number(form[3])
            form[4] = CheckForm.control_time(form[4])
            dict_tournament = {
                "name": form[0],
                "place": form[1],
                "date": form[2],
                "duration": form[3],
                "time_control": form[4],
                "description": form[5],
                "nb_rounds": NB_ROUNDS,
                "rounds": [],
                "players": [],
                "ended": "no",
            }
            print("Le tournoi a été créé avec succès.\n")
            return models.Tournament(dict_tournament)

    @staticmethod
    def run_tournament():
        current_tournament = models.Tournament.return_last_tournament()
        while len(current_tournament.rounds) < NB_ROUNDS:
            TournamentControl.round_control()
            current_tournament = models.Tournament.return_last_tournament()

        current_tournament.set_ended()

        list_tournament = models.Tournament.all_tournaments()
        finished_tournament = list_tournament[-1]
        rankings = list(
            sorted(
                finished_tournament["players"], key=lambda i: i["score"], reverse=True
            )
        )
        choice = views.TournamentMenu.end_screen(finished_tournament, rankings)
        if choice == "1":
            MainControl.main()
        elif choice == "q":
            sys.exit()

    @staticmethod
    def round_control():
        tournament_instance = models.Tournament.return_last_tournament()
        tournament_instance.round_start()
        outcome = views.TournamentMenu.tournament_round(tournament_instance)
        if outcome == "q":
            sys.exit()
        else:
            tournament_instance.round_end(outcome)


class PlayerControl:
    def __init__(self):
        self.player_menu = views.PlayerMenu()
        self.player_model = models.Player()

    def main():
        condition = False
        while condition is False:
            choice = views.PlayerMenu.main()
            if choice == "1":
                if len(models.Player.list_not_participants()) == 0:
                    condition = True
                    print("Aucun joueur disponible : veuillez en créer.\n")
                    PlayerControl.create_player()
                else:
                    condition = True
                    PlayerControl.select_players()
            elif choice == "2":
                condition = True
                PlayerControl.create_player()
            elif choice == "q":
                sys.exit()

    def change_rank():
        is_on = True
        list_all = models.Player.list_abridged(models.Player.all())
        while is_on:
            print("CHANGER LE CLASSEMENT D'UN JOUEUR\n")
            selection = views.PlayerMenu.change_ranks(list_all)
            if selection == "q":
                sys.exit()
            elif selection == "r":
                print("Menu quitté.\n")
                is_on = False
                MainControl.main()
            elif selection[1].isnumeric() is False:
                print("Réponse invalide.")
            else:
                player = models.Player(selection[0])
                player.change_rank(int(selection[1]))

    def create_player():
        form = views.PlayerMenu.create_player()
        if form == "r":
            views.PlayerMenu.main()
        elif form == "q":
            sys.exit
        else:
            if CheckForm.check_date(form[2]) is False:
                print("Champs date de naissance :")
                new_date = CheckForm.correct_date(form[2])
                form[2] = new_date
            if CheckForm.check_gender(form[3]) is False:
                print("Champs genre :")
                form[3] = CheckForm.check_gender(form[3])
            if CheckForm.check_number(form[4]) is False:
                print("Champs classement :")
                form[4] = CheckForm.check_number(form[4])

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
            list_not_participant = models.Player.list_not_participants()
            selection = views.PlayerMenu.select_players(
                models.Player.list_abridged(list_not_participant),
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


class MainControl:
    def __init__(self):
        self.main_menu = views.MainMenu()
        self.tournament_menu = views.TournamentMenu()
        self.rankings_menu = views.Rankings()
        self.players_models = models.Player()
        self.tournament_models = models.Tournament()
        self.tournament_control = TournamentControl()
        self.player_control = PlayerControl()

    def main():
        result = views.MainMenu.main().lower()
        if result == "n":
            MainControl.create_tournament()

        elif result == "c":
            if len(models.Tournament.all_tournaments()) == 0:
                print("Aucun tournoi en cours ! Veuillez créer un tournoi.")
                MainControl.create_tournament()
            else:
                last_tournament = models.Tournament.return_last_tournament()
                if last_tournament.ended == "True":
                    print("Aucun tournoi en cours ! Veuillez créer un tournoi.")
                    MainControl.create_tournament()
                else:
                    TournamentControl.run_tournament()

        elif result == "r":
            MainControl.main_rankings()

        elif result == "u":
            PlayerControl.change_rank()
        elif result == "q":
            sys.exit()

    def create_tournament():
        tournament_instance = TournamentControl.create_tournament()
        while len(models.Player.list_participants()) < NB_PLAYERS:
            PlayerControl.main()
        for player_dict in models.Player.list_participants():
            player = models.Player(player_dict)
            tournament_instance.players.append(player)
        tournament_instance.save()
        TournamentControl.run_tournament()

    def main_rankings():
        choice = views.Rankings.main()
        if choice == "1":
            MainControl.player_rankings()
        elif choice == "2":
            MainControl.tournaments_rankings()
        elif choice == "r":
            MainControl.main()
        elif choice == "q":
            sys.exit()

    def player_rankings():
        list_all = models.Player.all()
        choice = views.Rankings.ranking_players()
        if choice == "1":
            MainControl.player_rankings_alpha(list_all)
        elif choice == "2":
            MainControl.player_rankings_rank()
        elif choice == "3":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit

    def player_rankings_alpha(list_all):
        list_alpha = models.Player.alphabetical_list(list_all)
        choice = views.Rankings.ranking_players_alpha(list_alpha)
        if choice == "1":
            MainControl.player_rankings_rank()
        elif choice == "2":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit()

    def player_rankings_rank():
        list_ranked = models.Player.rank_list()
        choice = views.Rankings.ranking_players_rank(list_ranked)
        if choice == "1":
            MainControl.player_rankings_alpha(list_ranked)
        elif choice == "2":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit()

    def tournaments_rankings():
        list_tournament = models.Tournament.all_tournaments()
        choice = views.Rankings.ranking_tournaments(list_tournament)
        if choice == "r":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit()
        else:
            MainControl.tournament_rankings(list_tournament[choice - 1])

    def tournament_rankings(tournament):
        choice = views.Rankings.ranking_tournament(tournament)
        if choice == "1":
            MainControl.participants_alpha(tournament)
        elif choice == "2":
            MainControl.participants_by_rank(tournament)
        elif choice == "3":
            MainControl.rounds_rankings(tournament)
        elif choice == "4":
            MainControl.tournaments_rankings()
        elif choice == "q":
            sys.exit()

    def participants_alpha(tournament):
        choice = views.Rankings.ranking_players_alpha(tournament["players"])
        if choice == "1":
            MainControl.participants_by_rank(tournament)
        elif choice == "2":
            MainControl.tournament_rankings(tournament)
        else:
            sys.exit()

    def participants_by_rank(tournament):
        choice = views.Rankings.ranking_players_rank(tournament["players"])
        if choice == "1":
            MainControl.participants_alpha(tournament)
        elif choice == "2":
            MainControl.tournament_rankings(tournament)
        else:
            sys.exit()

    def rounds_rankings(tournament):
        choice = views.Rankings.ranking_rounds(tournament)
        if choice == "1":
            MainControl.tournament_rankings(tournament)
        elif choice == "q":
            sys.exit()
