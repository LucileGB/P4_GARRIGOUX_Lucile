import gettext

from utils.texts import Texts, TextsRanking, TextsModels

gettext.install("P4", "/locale")


class InputMenu:
    def __init__(self, interrupts=["r", "q"]):
        self.interrupts = interrupts

    def validate(self, answer, right_answers):
        answer = answer.lower()
        if answer in self.interrupts or answer in right_answers:
            return True
        else:
            return False

    def ask_input(self, right_answers=[], prompt=None, max_range=False,
                is_float=False):
        answer = "placeholder"

        if prompt:
            print(prompt)

        while self.validate(answer, right_answers) is False:
            answer = input(_("Réponse : "))
            if max_range:
                if self.check_num_input(answer, max_range) == True:
                    if is_float == True:
                        return float(answer)
                    else:
                        return int(answer)

        return answer

    def check_num_input(self, answer, max_range):
        if answer.isnumeric():
            if int(answer) in range(1, max_range+1):
                return True

    def confirm_choice(self, prompt=Texts.confirm_choice):
        answer = self.ask_input(right_answers=["o", "y", "n"], prompt=prompt)

        if answer == "o" or answer == "y":
            return True
        if answer == "n":
            return False

class DisplayMenu:
    def display_players_ranked(self, title, list_players, by_score=False):
        """
        Prints a player list sorted by rank if by_score is False, and
        by score otherwise.
        """
        if by_score == False:
            criteria = "rank"
        else:
            criteria = "score"

        ranked = list(sorted(list_players,
                            key=lambda p: p[f"{criteria}"],
                            reverse=True))
        i = 0

        print(title)
        for player in list_players:
            self.display_player(player, i)
            rank = ranked.index(player) + 1

            if rank == 1:
                print(f"Classement : {player[criteria]} points (1ère place)")
            else:
                print(f"Classement : {player[criteria]} points ({rank}ème place)")
            i += 1

    def display_tournament(self, tournament):
        form = TextsModels.tournament_form
        attributes = list(tournament.values())
        tournament_dict = dict(zip(form, attributes))

        for key, value in tournament_dict.items():
            print(f"{key} {value}")

    def display_player(self, player, index, rank=False):
        print(f"\n{index+1}. {player['first_name']} {player['last_name']}")
        print(f"Date de naissance : {player['birth_date']}")

class Menu(InputMenu):
    @staticmethod
    def change_form(field_list=[]):
        """Take care of swapping one selected article in a list of answers
        with a new input from the user."""
        i = 1
        for item in field_list:
            print(f"{i}. {item}")
            i += 1

        while True:
            choice = input(
                "Veuillez taper le chiffre correspondant au champs à modifier.\n"
            )
            if choice.isnumeric() is True:
                if Menu.input_ok(range(1, len(field_list) + 1), int(choice)) is True:
                    new_answer = input("Veuillez entrer une nouvelle réponse.\n")
                    field_list[int(choice) - 1] = new_answer
                    return field_list

    @staticmethod
    def fill_form(prompts=[]):
        """Submit a list of prompts to the user, then returns the results.
        If Q or R are submitted, interrupts the process and return them
        immediately."""
        answers = []
        for prompt in prompts:
            answer = input(prompt)
            if answer.lower() == "q":
                return "q"
            if answer.lower() == "r":
                return "r"
            while len(answer) == 0:
                print("Veuillez remplir ce champs.")
                answer = input(prompt)
            answers.append(answer)
        return answers

    @staticmethod
    def input_new(prompt):
        while True:
            answer = input(prompt)
            while len(answer) == 0:
                answer = input(prompt)
            confirm = Menu.yes_no()
            if confirm is True:
                return answer

    @staticmethod
    def input_ok(right_answers, answer):
        """Check whether a given input is in a given list."""
        if answer in right_answers:
            return True
        else:
            return False

    @staticmethod
    def yes_no():
        # Devrait être adaptable en InputMenu
        answers = ["o", "n"]
        answer = ""
        while Menu.input_ok(answers, answer) is False:
            answer = input("Cela vous convient-il ? (o/n)\n").lower()
            if answer == "o" or answer == "oui":
                return True
            if answer == "n" or answer == "non":
                return False

    @staticmethod
    def print_results(fields, answers):
        dict = dict(zip(fields, answers))

        for key, value in dict.item:
            print(f"{key}{value}")


class PlayerMenu(DisplayMenu, InputMenu):
    @staticmethod
    def main():
        """Return user input for the main player menu."""
        prompt = input(Texts.menu_players).lower()
        return prompt

    @staticmethod
    def create_player():
        """Returns inputs from the player creation forms. If R or Q are typed,
        interrupts the process and returns them immediately."""
        form = TextsModels.player_form
        print(Texts.menu_create_player)
        results = Menu.fill_form(form)
        if results == "r":
            return "r"
        if results == "q":
            return "q"
        PlayerMenu.print_results(form, results)
        confirm = Menu.yes_no()
        while confirm is False:
            results = Menu.change_form(results)
            i = 1
            for item in results:
                print(f"{i}. {item}")
                i += 1
            confirm = Menu.yes_no()
        return results

    @staticmethod
    def select_players(player_list, participants_list):
        """Add players to a tournament's players field. If R or Q are typed,
        interrupts the process and returns them immediately."""
        length = len(participants_list)
        if length > 0:
            i = 0
            print("PARTICIPANTS :")
            for player in participants_list:
                self.display_player(player, i)
                i += 1

        selected = self.ask_input(max_range=length,
                                    prompt=Texts.select_players)
        #TODO: si ça bugue, ce sera ci-dessous
        player = player_list[int(selected) - 1]
        name = f"{player['first_name']} {player['last_name']}"
        print(f"Vous avez sélectionné {name}.")
        confirm = Menu.yes_no()
        if confirm is True:
            return player

    def change_ranks(self, player_list):
        length = len(player_list)


        player = player_list[int(selected) - 1]
        name = f"{player['first_name']} {player['last_name']}"
        print(f"Sélection : {name}.")
        new_rank = input("Veuillez taper son nouveau classement : ")
        confirm = Menu.yes_no()
        if confirm is True:
            result = (player, new_rank.lower())
            return result


class Rankings(InputMenu, DisplayMenu):
    def players_sorted(self, title, list_players):
        """Shows player list sorted per names (a) or per rankings (s)."""
        self.display_players_ranked(title, list_players)

        answer = self.ask_input(right_answers=["a", "s"],
                    prompt=TextsRanking.players_sorted)

        return answer

    def tournaments_list(self, list_tournament):
        """Shows a list of all tournaments."""
        nb_tournaments = len(list_tournament)
        i = 0

        for tournament in list_tournament:
            print(f"\nTOURNOI {i+1}")
            self.display_tournament(tournament)
            i += 1

        # TODO: variation de ask_input qui prend en charge une liste (arg list len?)
        answer = self.ask_input(max_range=nb_tournaments,
                                    prompt=TextsRanking.tournaments_list
                                    )

        return answer

    def tournament(self, tournament):
        """Tournament menu for rankings. The returned input allows access to
        the participants list or the list of rounds and matches."""
        answer = self.ask_input(right_answers=["a", "s", "d"],
                    prompt=TextsRanking.tournament)

        return answer

    def rounds(self, tournament):
        """Shows a list of rounds and matches for the chosen tournament."""
        attributes = list(tournament.values())
        for round in attributes[7]:
            i = 0
            print(f"\n{round['name'].upper()}")
            print(f"Début : {round['start']}\nFin : {round['end']}")
            for match in round["matches"]:
                print(f"MATCH {i+1}")
                player_one = f"{match[0][0]['first_name']} {match[0][0]['last_name']}"
                score_one = f"{match[0][1]}"
                player_two = f"{match[1][0]['first_name']} {match[1][0]['last_name']}"
                score_two = f"{match[1][1]}"
                print(
                    f"{player_one} (score final : {score_one}) et {player_two} (score final : {score_two})"
                )
                i += 1

        answer = self.ask_input(prompt=TextsRanking.rounds)

        return answer


class TournamentMenu(Menu):
    @staticmethod
    def create_tournament(from_c=False):
        """Accepts input for the tournament creation form. If R or Q is typed,
        returns this input immediately.
        If accessed from the 'c' command, which correspond to 'continue', prints
        a warning that there was no ongoing tournament."""
        form_tournament = TextsModels.tournament_form

        if from_c == True:
            print("* Aucun tournoi en cours ! Vous pouvez créer un nouveau tournoi ci-dessous : * \n\n")

        print(Texts.menu_tournament)
        results = Menu.fill_form(form_tournament)
        if results == "r":
            return "r"
        if results == "q":
            return "q"
        print("\n\nNOUVEAU TOURNOI :\n")
        Menu.print_results(form_tournament, results)

        confirm = Menu.yes_no()
        while confirm is False:
            results = Menu.change_form(results)
            i = 1
            for item in results:
                print(f"{i}. {item}")
                i += 1
            confirm = Menu.yes_no()
        return results

    @staticmethod
    def tournament_round(tournament):
        """Shows the current matches. Uses function
        TournamentMenu.enter_results_confirm to accepts input as to
        each match's outcome."""
        nb_round = len(tournament.rounds)
        current_round = tournament.rounds[nb_round - 1]
        i = 1
        print(f"{tournament.name.upper()}.\n")
        print(f"Round actuel : {current_round.name}")
        print(f"Début du round : {current_round.start}")
        print('A tout moment, vous pouvez quitter en tapant "Q".')
        for match in current_round.matches:
            player_one = f"{match[0][0].first_name} {match[0][0].last_name}"
            player_two = f"{match[1][0].first_name} {match[1][0].last_name}"
            print(
                f"{i}. {player_one} ({match[0][0].score}) contre {player_two} ({match[1][0].score})"
            )
            i += 1

        outcome = TournamentMenu.enter_results_confirm(current_round)
        return outcome

    @staticmethod
    def end_screen(tournament, list_players):
        """Shows the tournament's result, printing the winner on top."""
        right_answers = ["1", "q"]
        answer = ""

        print("SCORES FINAUX\n")
        self.display_players_ranked(tournament["name"], list_players,
                                    by_score=True)

        while Menu.input_ok(right_answers, answer) is False:
            answer = input(Texts.end_menu).lower()
        return answer

    @staticmethod
    def enter_results(round):
        """Display matches and accept input for their outcome."""
        proper_input = ["1", "2", "3", "q"]
        results_list = []
        i = 1
        for match in round.matches:
            result = ""
            player_one = f"{match[0][0].first_name} {match[0][0].last_name}"
            player_two = f"{match[1][0].first_name} {match[1][0].last_name}"
            print(f"\nMATCH {i} : {player_one} contre {player_two}")
            while Menu.input_ok(proper_input, result) is False:
                result = input(Texts.matches_instructions).lower()
                if result in proper_input:
                    if result == "q":
                        return "q"
                    else:
                        results_list.append(result)
                        i += 1
        return results_list

    @staticmethod
    def enter_results_confirm(round):
        while True:
            results_list = TournamentMenu.enter_results(round)
            if results_list == "q":
                return "q"
            confirm = Menu.yes_no()
            if confirm is True:
                return results_list
