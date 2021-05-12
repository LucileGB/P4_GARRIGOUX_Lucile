import texts

class Menus:
    def input_ok(self, right_answers, answer):
        """Check whether a given input is in a given list."""
        if answer in right_answers:
            return True
        else:
            return False

    def yes_no(self):
        answers = ["o", "oui", "n", "non"]
        answer = ""

        while self.input_ok(answers, answer) == False:
            answer = input("Cela vous convient-il ? (o/n)\n").lower()
            if answer == "o" or answer == "oui":
                return True
            if answer == "n" or answer == "non":
                return False

    def fill_form(self, prompts=[]):
        """Submit a list of prompts to the user, then returns the results."""
        answers = []
        for prompt in prompts:
            answer = input(prompt)
            answers.append(answer)
        return answers

    def change_form(self, list=[]):
        """Take care of swapping one selected article in a list of answers
        with a new input from the user."""
        i = 1
        for item in list:
            print(f"{i}. {item}")
            i += 1
        choice = 0
        while self.input_ok(range(1, len(list) + 1), int(choice)) == False:
            choice = input(
                "Veuillez taper le chiffre correspondant au champs à modifier.\n"
            )
        new_answer = input("Veuillez entrer une nouvelle réponse.\n")
        list.pop(int(choice) - 1)
        list.insert(int(choice) - 1, new_answer)
        answer = self.yes_no()
        if answer == True:
            j = 1
            for item in list:
                print(f"{j}. {item}")
                j += 1
            return list
        else:
            self.change_form(list)

    def print_results(self, fields, answers):
        i = 0
        for field in fields:
            print(f"{fields[i]}{answers[i]}")
            i += 1


class MainMenu(Menus):
    def main_menu(self):
        inputs = ["n", "c", "m", "r"]
        answer = ""
        while self.input_ok(inputs, answer) == False:
            print(texts.Texts.welcome_text)
            answer = input("Votre choix : ").lower()
        return answer


class TournamentMenu(Menus):
    def create_tournament(self):
        form_tournament = [
            "Nom : ",
            "Adresse : ",
            "Date : ",
            "Date de fin : ",
            "Contrôle de temps (bullet, blitz ou coup rapide) : ",
            "Notes ou descriptions : ",
        ]

        print(texts.Texts.menu_tournament)
        results = self.fill_form(form_tournament)
        self.print_results(form_tournament, results)

        answer = self.yes_no()
        if answer == True:
            return results
        else:
            while answer == False:
                results = self.change_form(results)
                j = 0
                for item in results:
                    print(f"{j}. {item}")
                    j += 1
                answer = self.yes_no()

    def tournament_round(self, tournament):
        nb_round = len(tournament.rounds)
        current_round = tournament.rounds[nb_round-1]
        i = 1

        print(f"Bienvenue dans {tournament.name}.\n")
        print(f"Round actuel : {current_round.name}")
        print(f"Début du round : {current_round.start}")
        for match in current_round.matches:
            print(f"{i}. {match[0][0].first_name} {match[0][0].last_name} contre {match[1][0].first_name} {match[1][0].last_name}")
            i += 1

        outcome = self.enter_results(tournament, current_round)
        return outcome

    def enter_results(self, tournament, round):
        results = []
        i = 1
        for match in round.matches:
            print(f"MATCH {i}")
            result = input(texts.Texts.matches_instructions)
            results.append(result)
            i += 1

        confirm = self.yes_no()
        if confirm == True:
            return results
        else:
            self.enter_results(tournament)


class PlayerMenu(Menus):
    def create_players(self):
        form_players = [
            "Prénom : ",
            "Nom de famille : ",
            "Date de naissance : ",
            "Genre : ",
            "Classement : ",
        ]

        print(texts.Texts.menu_create_players)
        results = self.fill_form(form_players)
        self.print_results(form_players, results)
        confirm = self.yes_no()
        if confirm == True:
            return results
        else:
            while confirm == False:
                results = self.change_form(results)
                i = 1
                for item in results:
                    print(f"{i}. {item}")
                    i += 1
                confirm = self.yes_no()

    def menu_players(self):
        answers = ["1", "2"]
        prompt = input(texts.Texts.menu_players)
        return prompt

    def menu_selection(self, player_list):
        player_list()
        print(texts.Texts.select_players)
        nb_selected = []
        while len(nb_selected) < 8:
            finished = input("Chiffre : ")
            nb_selected.append(finished)
            print(f"Joueurs sélectionnés : {nb_selected}")

        confirm = self.yes_no()
        if confirm == True:
            return nb_selected
        else:
            nb_selected.clear()
            self.menu_selection(player_list)

class Rankings(Menus):
    def main_rankings(self):
        right_answers = ["1", "2", "3"]
        answer = ""
        while self.input_ok(right_answers, answer) == False:
            answer = input(texts.Texts.rankings_main)
        return answer

    def ranking_players(self, list_players):
        right_answers = ["1", "2", "3"]
        answer = ""
        while self.input_ok(right_answers, answer) == False:
            print(list_players)
            answer = input(texts.Texts.rankings_players)
        return answer

    def ranking_tournaments(self):
#Afficher la liste des tournois façon sélection de joueurs
        right_answers = ["1", "2", "3"]
        answer = ""
        while input_ok(self, right_answers, answer) == False:
            input(texts.Texts.rankings_tournaments)
