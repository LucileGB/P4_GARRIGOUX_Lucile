welcome_text = """Bienvenue !
Veuillez taper la lettre correspondant à l'une des options suivantes :
-  N pour créer un nouveau tournoi ;
-  C pour continuer un tournoi en cours ;
-  M pour modifier les classements de joueurs ;
-  R pour consulter les rapports (classements de joueurs, tournois passés, etc).
"""
commands = """Pour retourner à l'écran précédent, tapez \"r\"."""
menu_tournament = """Bienvenue dans le menu de création de tournoi.
Pour créer un tournoi, veuillez taper les informations suivantes :"""
menu_players = """Bienvenue dans le menu de sélections de joueurs.
Si vous souhaitez créer un ou des nouveaux joueurs, tapez 1.
Sinon, tapez 2.\n"""
menu_create_players = """Bienvenue dans le menu de création de joueurs.
Pour créer un joueurs, veuillez taper les informations suivantes :"""
menu_rapport = """Bienvenue dans le menu de rapports.

"""


class Menus:
    def input_ok(self, inputs, answer):
        """Check whether a given input is in a given list."""
        if answer in inputs:
            return True
        else:
            return False

    def yes_no(self):
        answers = ["o", "oui", "n", "non"]
        choice = ""

        while self.input_ok(answers, choice.lower()) == False:
            choice = input("Cela vous convient-il ? (o/n)\n")
        if choice == "o" or choice == "oui":
            return True
        if choice == "n" or choice == "non":
            return False

    def fill_form(self, prompts=[]):
        """Submit a list of prompts of the user, then returns the results."""
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
        while self.input_ok(range(1, len(list)+1), int(choice)) == False:
            choice = input("Veuillez taper le chiffre correspondant au champs à modifier.\n")
        new_answer = input("Veuillez entrer une nouvelle réponse.\n")
        list.pop(int(choice)-1)
        list.insert(int(choice)-1, new_answer)
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
        while Menus.input_ok(self, inputs, answer) == False:
            print(welcome_text)
            answer = input("Votre choix : ").lower()

        if answer == "n":
            return "n"
        elif answer == "c":
            # reprendra au dernier round du dernier tournoi rentré dans la db
            pass
        elif answer == "m":
            # consultera la db pour afficher rapport(liste de joueur)
            pass
        elif answer == "r":
            #self.reports(self)
            pass

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

        print(menu_tournament)
        results = Menus.fill_form(self, form_tournament)
        Menus.print_results(self, form_tournament, results)

        answer = Menus.yes_no(self)
        if answer == True:
            # Téléphoner controller pour qu'il crée une instance de tournois
            # et génère un premier round, puis appelle un écran tournoi
            pass
        else:
            while answer == False:
                results = Menus.change_form(self, results)
                j = 0
                for item in results:
                    print(f"{j}. {item}")
                    j += 1
                answer = Menus.yes_no(self)

        def continue_tournament(self):
            pass

class PlayerMenu(Menus):
    def menu_players(self):
        answers = ["1", "2"]
        choice = ""
        while Menus.input_ok(self, answers, choice) == False:
            choice = input(menu_players)
        confirm = Menus.yes_no(self)
        if confirm == True:
            if choice == "1":
                #Créer écran character selection
                self.player_selection()
            else:
                return "2"
        else:
            self.menu_players()

        def player_selection(self):
            pass

class CreatePlayer(Menus):
    def create_players(self):
        form_players = [
            "Prénom : ",
            "Nom de famille : ",
            "Date de naissance : ",
            "Genre : ",
            "Classement : ",
        ]

        print(commands)
        print(menu_create_players)
        results = self.fill_form(form_players)
        self.print_results(form_players, results)

        answer = self.yes_no()
        if answer == True:
            # Téléphoner controller pour qu'il crée une instance de tournois
            # et génère un premier round, puis appelle un écran tournoi
            pass
        else:
            while answer == False:
                results = self.change_form(results)
                i = 1
                for item in results:
                    print(f"{i}. {item}")
                    i += 1
                answer = self.yes_no()

class Reports(Menus):
    def reports(self):
        inputs = ["sa mère"]
