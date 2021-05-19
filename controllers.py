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
        if attributes == "q":
            sys.exit
        elif attributes == "r":
            MainControl.main()
        else:
            instance_tournament = models.Tournament(
                attributes[0], attributes[1], attributes[2], attributes[3],
                attributes[4], attributes[5]
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

    def change_rank():
        is_on = True
        list_all = models.Player.list_abridged(models.Player.all())
        while is_on == True:
            print("CHANGER LE CLASSEMENT D'UN JOUEUR\n")
            selection = views.PlayerMenu.change_players_ranks(list_all)
            if selection == "q":
                sys.exit()
            elif selection == "r":
                print("Menu quitté.\n")
                is_on == False
                MainControl.main()
            else:
                first_name = selection[0]["first_name"]
                last_name = selection[0]["last_name"]
                birth_date = selection[0]["birth_date"]
                models.Player.change_rank(first_name, last_name,
                                        birth_date, int(selection[1]))

    def create_player():
        attributes = views.PlayerMenu.create_player()
        if attributes == "r":
            views.PlayerMenu.main()
        elif attributes == "q":
            sys.exit
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
            selection = views.PlayerMenu.select_players(
                models.Player.list_abridged(models.Player.list_not_participants())
            )
            if selection == "q":
                sys.exit()
            elif selection == "r":
                print("Menu quitté.\n")
                is_on == False
                PlayerControl.main()
            elif selection > len(models.Player.list_participants()):
                print("Ce nombre ne correspond à aucun joueur.")
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
            TournamentControl.launch_tournament()

        elif result == "r":
            MainControl.main_rankings()

        elif result == "u":
            ControlPlayer.change_rank()
        elif result == "q":
            sys.exit()

    def main_rankings():
        choice = views.Rankings.main_rankings()
        if choice == "1":
            MainControl.player_rankings()
        elif choice == "2":
            MainControl.tournaments_rankings()
        elif choice == "3":
            MainControl.main()
        elif choice == "q":
            sys.exit

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
            sys.exit

    def player_rankings_rank():
        list_ranked = models.Player.rank_list()
        choice = views.Rankings.ranking_players_rank(list_ranked)
        if choice == "1":
            MainControl.player_rankings_alpha()
        elif choice == "2":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit

    def tournaments_rankings():
        list_tournament = models.Tournament.all_tournaments()
        choice = views.Rankings.ranking_tournaments(list_tournament)
        if choice == "r":
            MainControl.main_rankings()
        elif choice == "q":
            sys.exit
        else:
            MainControl.tournament_rankings(list_tournament[choice-1])

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
            sys.exit

    def participants_by_rank(tournament):
        choice = views.Rankings.ranking_players_rank(tournament["Participants"])
        if choice == "1" :
            MainControl.participants_alpha(tournament)
        elif choice == "2":
            MainControl.tournament_rankings(tournament)
        else:
            sys.exit

    def participants_alpha(tournament):
        choice = views.Rankings.ranking_players_alpha(tournament["Participants"])
        if choice == "1" :
            MainControl.participants_by_rank(tournament)
        elif choice == "2":
            MainControl.tournament_rankings(tournament)
        else:
            sys.exit

    def rounds_rankings(tournament):
        choice = views.Rankings.ranking_rounds(tournament)
        if choice == "1":
            MainControl.tournament_rankings(tournament)
        elif choice == "q":
            sys.exit
