from texts import Texts


class Menu:
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
            if choice.isnumeric() == True:
                if Menu.input_ok(range(1, len(field_list) + 1), int(choice)) == True:
                    new_answer = input("Veuillez entrer une nouvelle réponse.\n")
                    field_list.pop(int(choice) - 1)
                    field_list.insert(int(choice) - 1, new_answer)
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
            if confirm == True:
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
        answers = ["o", "n"]
        answer = ""
        while Menu.input_ok(answers, answer) == False:
            answer = input("Cela vous convient-il ? (o/n)\n").lower()
            if answer == "o" or answer == "oui":
                return True
            if answer == "n" or answer == "non":
                return False

    @staticmethod
    def print_results(fields, answers):
        i = 0
        for field in fields:
            print(f"{fields[i]}{answers[i]}")
            i += 1


class MainMenu(Menu):
    @staticmethod
    def main():
        inputs = ["n", "c", "m", "r", "q"]
        answer = ""
        while Menu.input_ok(inputs, answer) == False:
            print(Texts.welcome_text)
            answer = input("Votre choix : ").lower()
        return answer


class PlayerMenu(Menu):
    @staticmethod
    def main():
        """Return user input for the main player menu."""
        prompt = input(Texts.menu_players).lower()
        return prompt

    @staticmethod
    def create_player():
        """Returns inputs from the player creation forms. If R or Q are typed,
        interrupts the process and returns them immediately."""
        form_players = [
            "Prénom : ",
            "Nom de famille : ",
            "Date de naissance (format : jour/mois/année) : ",
            "Genre (homme/femme): ",
            "Classement (nombre total de points): ",
        ]
        print(Texts.menu_create_player)
        results = Menu.fill_form(form_players)
        if results == "r":
            return "r"
        if results == "q":
            return "q"
        PlayerMenu.print_results(form_players, results)
        confirm = Menu.yes_no()
        while confirm == False:
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
        print(Texts.select_players)
        if len(participants_list) > 0:
            i = 0
            print(f"PARTICIPANTS :")
            for player in participants_list:
                name = f"{player['first_name']} {player['last_name']}"
                print(f"Joueur {i+1} : {name}")
                i += 1
        has_chosen = False
        while has_chosen == False:
            selected = input("Chiffre : ")
            if selected.lower() == "q":
                return "q"
            elif selected.lower() == "r":
                return "r"
            elif selected.isnumeric() == False:
                print("Veuillez taper un chiffre.")
            elif int(selected) > len(player_list):
                print("Ce nombre ne correspond à aucun joueur.")
            else:
                player = player_list[int(selected) - 1]
                name = f"{player['first_name']} {player['last_name']}"
                print(f"Vous avez sélectionné {name}.")
                confirm = Menu.yes_no()
                if confirm == True:
                    return player

    @staticmethod
    def change_ranks(player_list):
        has_chosen = False
        while has_chosen == False:
            print("Sélection d'un joueur :")
            selected = input(Texts.new_number)
            if selected == "q":
                return "q"
            if selected == "r":
                return "r"
            elif selected.isnumeric() == False:
                print("Veuillez taper un chiffre.")
            elif selected.isnumeric() == True and (int(selected) - 1) > len(
                player_list
            ):
                print("Ce nombre ne correspond à aucun joueur.")
            else:
                player = player_list[int(selected) - 1]
                name = f"{player['first_name']} {player['last_name']}"
                print(f"Sélection : {name}.")
                new_rank = input("Veuillez taper son nouveau classement : ")
                confirm = Menu.yes_no()
                if confirm == True:
                    result = (player, new_rank.lower())
                    return result


class Rankings(Menu):
    @staticmethod
    def main():
        right_answers = ["1", "2", "r", "q"]
        answer = ""
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_main).lower()
        return answer

    @staticmethod
    def ranking_players():
        right_answers = ["1", "2", "3", "q"]
        answer = ""
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_players).lower()
        return answer

    @staticmethod
    def show_list(list_players):
        i = 0
        rankings = list(sorted(list_players, key=lambda i: i["rank"], reverse=True))
        for player in list_players:
            rank = ""
            for player_r in rankings:
                if player == player_r:
                    rank = rankings.index(player_r) + 1

            print(f"\n{i+1}. {player['first_name']} {player['last_name']}")
            print(f"Date de naissance : {player['birth_date']}")
            print(f"Genre : {player['gender']}")
            if rank == 1:
                print(f"Classement : {player['rank']} points (1ère place)")
            else:
                print(f"Classement : {player['rank']} points ({rank}ème place)")
            i += 1

    @staticmethod
    def ranking_players_alpha(list_players):
        """Shows the player list in alphabetical order."""
        right_answers = ["1", "2", "q"]
        answer = ""
        print("JOUEURS PAR ORDRE ALPHABETIQUE\n")
        Rankings.show_list(list_players)

        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_players_alpha).lower()
        return answer

    @staticmethod
    def ranking_players_rank(list_players):
        """Shows the player list per rankings."""
        right_answers = ["1", "2", "q"]
        answer = ""
        print("JOUEURS PAR CLASSEMENT\n")
        Rankings.show_list(list_players)
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_players_rank).lower()
        return answer

    @staticmethod
    def ranking_tournaments(list_tournament):
        """Shows a list of all tournaments."""
        right_answers = ["r", "q"]
        nb_tournaments = len(list_tournament)
        answer = ""
        i = 0
        form = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Durée (en jours) : ",
            "Contrôle de temps : ",
            "Notes ou descriptions : ",
        ]
        for tournament in list_tournament:
            attributes = list(tournament.values())
            j = 0
            print(f"TOURNOI {i+1}")
            for field in form:
                print(f"{field}{attributes[j]}")
                j += 1
            i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_tournaments).lower()
            if answer.isnumeric() == True:
                if int(answer) in range(0, nb_tournaments + 1):
                    return int(answer)
        return answer

    @staticmethod
    def ranking_tournament(tournament):
        """Tournament menu for rankings. The returned input allow access to
        the participants list or the list of rounds and matches."""
        right_answers = ["1", "2", "3", "4", "q"]
        answer = ""
        i = 0
        attributes = list(tournament.values())
        form = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Date de fin : ",
            "Contrôle de temps : ",
            "Notes ou descriptions : ",
        ]
        for field in form:
            print(f"{field}{attributes[i]}")
            i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.ranking_tournament).lower()
        return answer

    @staticmethod
    def ranking_rounds(tournament):
        """Shows a list of rounds and matches for the chosen tournament."""
        right_answers = ["1", "q"]
        answer = ""
        attributes = list(tournament.values())
        for round in attributes[7]:
            i = 0
            rounds_attr = list(round.values())
            print(f"\n{rounds_attr[0].upper()}")
            print(f"Début : {rounds_attr[1]}")
            print(f"Fin : {rounds_attr[2]}")
            for match in rounds_attr[3]:
                player_one = f"{match[0][0]['first_name']} {match[0][0]['last_name']}"
                score_one = f"{match[0][1]}"
                player_two = f"{match[1][0]['first_name']} {match[1][0]['last_name']}"
                score_two = f"{match[1][1]}"
                print(f"MATCH {i+1}")
                print(
                    f"{player_one} (score final : {score_one}) et {player_two} (score final : {score_two})"
                )
                i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.ranking_rounds).lower()
        return answer


class TournamentMenu(Menu):
    @staticmethod
    def create_tournament():
        """Accepts input for the tournament creation form. If R or Q is typed,
        returns this input immediately."""
        form_tournament = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Durée (en jours, en chiffre) : ",
            "Contrôle de temps :\n1. Bullet\n2. Blitz\n3. Coup rapide\n",
            "Notes ou descriptions : ",
        ]

        print(Texts.menu_tournament)
        results = Menu.fill_form(form_tournament)
        if results == "r":
            return "r"
        if results == "q":
            return "q"
        print("\n\nNOUVEAU TOURNOI :\n")
        Menu.print_results(form_tournament, results)

        answer = Menu.yes_no()
        if answer == True:
            return results
        else:
            while answer == False:
                results = Menu.change_form(results)
                j = 0
                for item in results:
                    print(f"{j}. {item}")
                    j += 1
                answer = Menu.yes_no()

    @staticmethod
    def tournament_round(tournament):
        """Shows the current matches. Uses function
        TournamentMenu.enter_results_confirm to accepts input as to
        each match's outcome."""
        nb_round = len(tournament.rounds)
        current_round = tournament.rounds[nb_round - 1]
        i = 1
        print(f"Bienvenue dans {tournament.name}.\n")
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
    def end_screen(tournament):
        """Shows the tournament's result, printing the winner on top."""
        right_answers = ["1", "q"]
        answer = ""
        attributes = list(tournament.values())
        player_rank = 0
        rankings = list(sorted(attributes[8], key=lambda i: i["score"], reverse=True))
        print("SCORES FINAUX\n")
        for player in rankings:
            player_attributes = list(player.values())
            if player_rank == 0:
                print("GAGNANT :")
                print(f"\n{i+1}. {attributes[0]} {attributes[1].upper()}")
                print(f"Classement : {attributes[4]} points\n\n")
            else:
                print(f"{player_rank+1} place :")
                player_attributes = list(player.values())
                print(f"\n{i+1}. {attributes[0]} {attributes[1].upper()}")
                print(f"Classement : {attributes[4]} points\n")
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.rankings_players_rank)
        return answer.lower()

        for round in attributes[7]:
            i = 0
            rounds_attr = list(round.values())
            print(f"\n{rounds_attr[0].upper()}")
            print(f"Début : {rounds_attr[1]}")
            print(f"Durée : {rounds_attr[2]}")
            for match in rounds_attr[3]:
                player_one = f"{match[0][0]['first_name']} {match[0][0]['last_name']}"
                score_one = f"{match[0][1]}"
                player_two = f"{match[1][0]['first_name']} {match[1][0]['last_name']}"
                score_two = f"{match[1][1]}"
                print(f"MATCH {i+1}")
                print(
                    f"{player_one} (score final : {score_one}) et {player_two} (score final : {score_two})"
                )
                i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(Texts.ranking_rounds).lower()
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
            while Menu.input_ok(proper_input, result) == False:
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
            if confirm == True:
                return results_list
