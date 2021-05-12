import models
import views

current_tournament = None
class RoundControl:
    def __init__(self):
        self.tournament_menu = views.TournamentMenu()
        self.tournament_model = models.Tournament()

class TournamentControl:
    def __init__(self):
        self.tournament_menu = views.TournamentMenu()
        self.tournament_model = models.Tournament()

    def create_tournament(self):
        global current_tournament
        attributes = self.tournament_menu.create_tournament()
        #ADD VERIFICATION
        current_tournament = models.Tournament(attributes[0],
                        attributes[1], attributes[2],
                        attributes[3], attributes[4])

    def launch_tournament(self):
#rename launch_tournament
        i = 0
        global current_tournament
        current_tournament = self.tournament_model.return_last_tournament()
        current_tournament.new_round()
        outcome = self.tournament_menu.tournament_round(current_tournament)
        round = current_tournament.rounds[-1]
        for match in round.matches:
            match = models.Match(match)
            match.set_result(int(outcome[i]))
            i += 1
        current_tournament.finish_round()
        if len(current_tournament.rounds) <= 4:
            self.launch_tournament()
        else:
            print("Résultats du tournoi :")
            print(final_ranking_list)


class PlayerControl:
    def __init__(self):
        self.player_menu = views.PlayerMenu()
        self.player_model = models.Player()

    def main_player_menu(self):
        choice = self.player_menu.menu_players()
        if choice == "1":
            self.select_players()
            return
        if choice == "2":
            self.create_player()
        else:
            self.main_player_menu()

    def select_players(self):
        global current_tournament
        selection = self.player_menu.menu_selection(
            self.player_model.show_all_abridged)
# ADD VERIFICATION
        for player in selection:
            participant = self.player_model.add_participant(int(player))
            current_tournament.add_player(participant)

    def create_player(self):
        attributes = self.player_menu.create_players()
# ADD VERIFICATION
        new_player = models.Player(attributes[0], attributes[1],
                                    attributes[2], attributes[3])
        new_player.table_insert_player()
        self.main_player_menu()


class MainControl:
    def __init__(self):
        self.main_menu = views.MainMenu()
        self.tournament_menu = views.TournamentMenu()
        self.rankings_menu = views.Rankings()
        self.players_models =  models.Player()
        self.tournament_models = models.Tournament()
        self.tournament_control = TournamentControl()
        self.player_control = PlayerControl()

    def main(self):
        global current_tournament
        result = self.main_menu.main_menu().lower()
        if result == "n":
            self.tournament_control.create_tournament()
            self.player_control.main_player_menu()
            current_tournament.serialize_tournament()
            self.tournament_control.launch_tournament()

        elif result == "c":
        # reprendra au dernier round du dernier tournoi rentré dans la db
            self.tournament_control.launch_tournament()

        elif result == "r":
            self.main_rankings()

    def main_rankings(self):
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
