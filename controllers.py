import sys

import helper
import models
import texts
import views


current_tournament = None


class TournamentControl:
    def __init__(self):
        self.tournament_menu = views.TournamentMenu()
        self.tournament_model = models.Tournament()

    def create_tournament():
        models.Player.clear_participants()
        attributes = views.TournamentMenu.create_tournament()
        # ADD VERIFICATION
        instance_tournament = models.Tournament(
            attributes[0], attributes[1], attributes[2], attributes[3], attributes[4]
        )
        return instance_tournament

    @staticmethod
    def launch_tournament():
        # rename launch_tournament
        i = 0
        current_tournament = models.Tournament.return_last_tournament()
        while len(current_tournament.rounds) < 4:
            TournamentControl.round_control()

        print("Résultats du tournoi :")

    @staticmethod
    def round_control():
        tournament = models.Tournament.return_last_tournament()
        tournament.round_start()
        outcome = views.TournamentMenu.tournament_round(tournament)
        if outcome == "q":
            sys.exit()
        else:
            tournament.round_end(outcome)

class PlayerControl:
    def __init__(self):
        self.player_menu = views.PlayerMenu()
        self.player_model = models.Player()

    def main():
        chose = False
        while chose == False:
            choice = views.PlayerMenu.main()
            if choice == "1":
                chose = True
                PlayerControl.select_players()
            elif choice == "2":
                chose = True
                PlayerControl.create_player()
            elif choice == "q":
                sys.exit()

    def create_player():
        attributes = views.PlayerMenu.create_player()
        if attributes == "r":
            views.PlayerMenu.main()
        else:
            if helper.CheckForm.check_date(attributes[2]) == False:
                attributes[2] == views.Menu.input_new(texts.Texts.player_new_date)
            if helper.CheckForm.check_gender(attributes[3]) == False:
                attributes[3] == views.Menu.input_new(texts.Texts.player_new_gender)
            if helper.CheckForm.check_rank(attributes[4]) == False:
                attributes[3] == views.Menu.input_new(texts.Texts.player_new_rank)

            new_player = models.Player(
                attributes[0],
                attributes[1],
                attributes[2],
                attributes[3],
                attributes[4],
            )
            if new_player.has_double() == True:
                print("Ce joueur existe déjà.\n")
                views.PlayerMenu.main()
            else:
                new_player.table_insert_player()
                print("Le joueur a été créé avec succès.\n")
                PlayerControl.main()

    def select_players():
        is_on = True
        list_not_participant = models.Player.list_not_participants()
        while is_on == True and len(models.Player.list_participants()) < 8:
            print(len(models.Player.list_participants()))
            selection = views.PlayerMenu.select_players(
                models.Player.list_abridged(models.Player.list_not_participants())
            )
            if selection == "q":
                sys.exit()
            elif selection == "r":
                print("Menu quitté.\n")
                is_on == False
                PlayerControl.main()
            else:
                first_name = selection["first_name"]
                last_name = selection["last_name"]
                birth_date = selection["birth_date"]
                models.Player.is_playing_true(first_name, last_name, birth_date)


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
        result = views.MainMenu.main_menu().lower()
        if result == "n":
            tournament_instance = TournamentControl.create_tournament()
            while len(models.Player.list_participants()) < 8:
                PlayerControl.main()
            for player_dict in models.Player.list_participants():
                player = models.Player.instantiate_player(player_dict)
                tournament_instance.players.append(player)
            tournament_instance.serialize_tournament()
            TournamentControl.launch_tournament()

        elif result == "c":
            # reprendra au dernier round du dernier tournoi rentré dans la db
            TournamentControl.launch_tournament()

        elif result == "r":
            MainControl.main_rankings()

        elif result == "q":
            sys.exit()

    def main_rankings():
        choice = self.rankings_menu.main_rankings()
        if choice == "1":
            list = models.Player.alphabetical_list()
            self.player_rankings_alpha()
        elif choice == "2":
            pass
        elif choice == "3":
            self.main()

    def player_rankings_alpha(self):
        list = models.Player.alphabetical_list()
        choice = self.rankings_menu.ranking_players(list)
        if choice == "1":
            self.player_rankings_alpha()
        elif choice == "2":
            self.player_rankings_rank()
        elif choice == "3":
            self.main_rankings()

    def player_rankings_rank(self):
        list = models.Player.rank_list()
        choice = self.rankings_menu.ranking_players(list)
        if choice == "1":
            self.player_rankings_alpha()
        elif choice == "2":
            self.player_rankings_rank()
        elif choice == "3":
            self.main_rankings()
