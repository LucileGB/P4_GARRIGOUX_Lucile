import texts


class Menu:
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

    def fill_form(prompts=[]):
        """Submit a list of prompts to the user, then returns the results."""
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

    def input_new(prompt):
        while True:
            answer = input(prompt)
            while len(answer) == 0:
                answer = input(prompt)
            confirm = Menu.yes_no()
            if confirm == True:
                return answer

    def input_ok(right_answers, answer):
        """Check whether a given input is in a given list."""
        if answer in right_answers:
            return True
        else:
            return False

    def yes_no():
        answers = ["o", "n"]
        answer = ""
        while Menu.input_ok(answers, answer) == False:
            answer = input("Cela vous convient-il ? (o/n)\n").lower()
            if answer == "o" or answer == "oui":
                return True
            if answer == "n" or answer == "non":
                return False

    def print_results(fields, answers):
        i = 0
        for field in fields:
            print(f"{fields[i]}{answers[i]}")
            i += 1


class MainMenu(Menu):
    def main_menu():
        inputs = ["n", "c", "m", "r", "q"]
        answer = ""
        while Menu.input_ok(inputs, answer) == False:
            print(texts.Texts.welcome_text)
            answer = input("Votre choix : ").lower()
        return answer


class PlayerMenu(Menu):
    def create_player():
        form_players = [
            "Prénom : ",
            "Nom de famille : ",
            "Date de naissance (format : jour/mois/année) : ",
            "Genre (homme/femme): ",
            "Classement (nombre total de points): ",
        ]
        print(texts.Texts.menu_create_player)
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

    def main():
        answers = ["1", "2", "q"]
        prompt = input(texts.Texts.menu_players).lower()
        return prompt

    def select_players(player_list):
        print(texts.Texts.select_players)
        has_chosen = False
        while has_chosen == False:
            selected = input("Chiffre : ")
            if selected == "q":
                return "q"
            if selected == "r":
                return "r"
            elif selected.isnumeric() == False:
                print("Veuillez taper un chiffre.")
            else:
                player = player_list[int(selected)]
                name = f"{player['first_name']} {player['last_name']}"
                print(f"Vous avez sélectionné {name}.")
                confirm = Menu.yes_no()
                if confirm == True:
                    return player

    def change_players_ranks(player_list):
        has_chosen = False
        while has_chosen == False:
            print(texts.Texts.menu_change_ranks)
            selected = input("Chiffre : ")
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
                    result = (player, new_rank)
                    return result


class Rankings(Menu):
    def main_rankings():
        right_answers = ["1", "2", "3", "q"]
        answer = ""
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(texts.Texts.rankings_main)
        return answer.lower()

    def ranking_players():
        right_answers = ["1", "2", "3", "q"]
        answer = ""
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(texts.Texts.rankings_players).lower()
        return answer

    def ranking_players_alpha(list_players):
        right_answers = ["1", "2", "q"]
        answer = ""
        i = 0
        rankings = list(sorted(list_players, key=lambda i: i["rank"], reverse=True))
        print("JOUEURS PAR ORDRE ALPHABETIQUE\n")
        for player in list_players:
            rank = ""
            for player_r in rankings:
                if player == player_r:
                    rank = rankings.index(player_r) + 1

            attributes = list(player.values())
            print(f"\n{i}. {attributes[0]} {attributes[1].upper()}")
            print(f"Date de naissance : {attributes[2]}")
            print(f"Genre : {attributes[3]}")
            if rank == 1:
                print(f"Classement : {attributes[4]} points (1ère place)")
            else:
                print(f"Classement : {attributes[4]} points ({rank}ème place)")
            i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(texts.Texts.rankings_players_alpha)
        return answer.lower()

    def ranking_players_rank(list_players):
        right_answers = ["1", "2", "q"]
        answer = ""
        i = 0
        rankings = list(sorted(list_players, key=lambda i: i["rank"], reverse=True))
        print("JOUEURS PAR CLASSEMENT\n")
        for player in list_players:
            attributes = list(player.values())
            rank = ""
            for player_r in rankings:
                if player == player_r:
                    rank = rankings.index(player_r) + 1

            print(f"\n{i+1}. {attributes[0]} {attributes[1].upper()}")
            print(f"Date de naissance : {attributes[2]}")
            print(f"Genre : {attributes[3]}")
            if rank == 1:
                print(f"Classement : {attributes[4]} points (1ère place)")
            else:
                print(f"Classement : {attributes[4]} points ({rank}ème place)")
            i += 1
        while Menu.input_ok(right_answers, answer) == False:
            answer = input(texts.Texts.rankings_players_rank)
        return answer.lower()

    def ranking_tournaments(list_tournament):
        right_answers = ["r", "q"]
        nb_tournaments = len(list_tournament)
        answer = ""
        i = 0
        form = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Date de fin : ",
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
            answer = input(texts.Texts.rankings_tournaments).lower()
            if answer.isnumeric() == True:
                if int(answer) in range(0, nb_tournaments + 1):
                    return int(answer)
        return answer

    def ranking_tournament(tournament):
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
            answer = input(texts.Texts.ranking_tournament).lower()
        return answer

    def ranking_rounds(tournament):
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
            answer = input(texts.Texts.ranking_rounds).lower()
        return answer
        print(tournament)


class TournamentMenu(Menu):
    @staticmethod
    def create_tournament():
        form_tournament = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Date de fin : ",
            "Contrôle de temps (bullet, blitz ou coup rapide) : ",
            "Notes ou descriptions : ",
        ]

        print(texts.Texts.menu_tournament)
        results = Menu.fill_form(form_tournament)
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
        nb_round = len(tournament.rounds)
        current_round = tournament.rounds[nb_round - 1]
        print(f"tournament_round: {current_round.matches}")
        print(f"tournament_round: {len(current_round.matches)}")
        i = 1
        print(f"Bienvenue dans {tournament.name}.\n")
        print(f"Round actuel : {current_round.name}")
        print(f"Début du round : {current_round.start}")
        print('A tout moment, vous pouvez quitter en tapant "Q".')
        for match in current_round.matches:
            player_one = f"{match[0][0].first_name} {match[0][0].last_name}"
            player_two = f"{match[1][0].first_name} {match[1][0].last_name}"
            print(
                f"{i}. {player_one}, {match[0][0].score} contre {player_two}, {match[1][0].score}"
            )
            i += 1

        outcome = TournamentMenu.enter_results_confirm(tournament, current_round)
        return outcome

    @staticmethod
    def enter_results(tournament, round):
        proper_input = ["1", "2", "3", "q"]
        results_list = []
        i = 1
        for match in round.matches:
            result = ""
            player_one = f"{match[0][0].first_name} {match[0][0].last_name}"
            player_two = f"{match[1][0].first_name} {match[1][0].last_name}"
            print(f"\nMATCH {i} : {player_one} contre {player_two}")
            while Menu.input_ok(proper_input, result) == False:
                result = input(texts.Texts.matches_instructions).lower()
                if result in proper_input:
                    if result == "q":
                        return "q"
                    else:
                        results_list.append(result)
                        i += 1
        return results_list

    @staticmethod
    def enter_results_confirm(tournament, round):
        while True:
            results_list = TournamentMenu.enter_results(tournament, round)
            if results_list == "q":
                return "q"
            confirm = Menu.yes_no()
            if confirm == True:
                return results_list
