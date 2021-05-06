import datetime
from tinydb import TinyDB, Query

NB_PLAYERS = 8
NB_ROUNDS = 4

db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")
rounds_table = db.table("rounds")

class Match:
    def __init__(self, players=([], [])):
        self.players = players

    def set_result(self, winner):
        # 1 and 2 grant 1 points to the winner. 3 means a tie.
        if winner == 1:
            self.players[0][1] += 1
        elif winner == 2:
            self.players[1][1] += 1
        else:
            self.players[0][1] += 0.5
            self.players[1][1] += 0.5


class Round:
    def __init__(self, name, id, start=None, end=None, matches=[]):
        self.name = name
        self.start = start
        self.end = end
        self.matches = matches

    def time_now():
        time = datetime.datetime.now()
        time = time.strftime("%d/%m/%Y à %H:%M")
        return time

    def create_matches(self, player_list):
        # past_matches = all the matches in the previous rounds
        past_matches = []
        higher_tier = []
        i = 0
        while len(higher_tier) < len(player_list):
            higher_tier.append(player_list[0])
            player_list.pop(0)
        while i + 1 <= len(higher_tier):
            match = (
                [higher_tier[i], higher_tier[i].score],
                [player_list[i], player_list[i].score],
            )
            for old_match in past_matches:
                if match[0][0] in old_match and match[0][1] in old_match:
                    match = (
                        [higher_tier[i], higher_tier[i].score],
                        [player_list[i + 1], player_list[i + 1].score],
                    )
            self.matches.append(match)
            i += 1

    # insérer les matches dans la DB

    def classify_list(self, liste_players):
        liste_players = sorted(liste_players, key=lambda Player: Player.score)
        for player in liste_players:
            for other_player in liste_players:
                if (
                    player.score == other_player.score
                    and player.rank < other_player.rank
                ):
                    current_index = index(player)
                    new_index = index(other_player)
                    liste_player.insert(new_index, player)
                    liste_player.pop(current_index)


class Tournament:
    def __init__(
        self,
        name,
        place,
        date,
        end,
        time_control,
        description=None,
        nb_rounds=NB_ROUNDS,
        rounds=[],
        players=[],
    ):
        self.name = name
        self.place = place
        self.date = date
        self.end = end
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.players = players

    def new_round(self, liste_players):
        nb_round = len(self.rounds) + 1
        round = Round(f"Round {nb_round}", f"{self.date}",
                        start=Round.time_now())
        self.rounds.append(round)
        # sauvegarder le nouveau round dans db


class Player:
    def __init__(self, first_name, last_name, birth_date, gender,
                rank=0, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score

    def serialize_player(self):
        serialized_player = {"Prenom": self.first_name, "Nom":
                            self.last_name,
                            "Date de naissance": self.birth_date,
                            "Genre": self.gender, "Classement": self.rank,
                            "Score": self.score
                            }
        players_table.insert(serialized_player)

    def instantiate_player(first_name, last_name):
        for player in players_table:
            attributes = list(player.values())
            result = Player(attributes[0], attributes[1], attributes[2],
                            attributes[3], attributes[4], attributes[5])
            return result

    def search_player(first_name, last_name):
        Players = Query()
        result = players_table.search(Players.Prenom == first_name
                                        and Players.Nom == last_name)
        if len(result) == 0:
            return False
        else:
            return result

    def fetch_all_players():
        i = 0
        for player in players_table:
            j = 0
            keys = list(player.keys())
            attributes = list(player.values())
            print(f"\n{i}. {attributes[0].upper()} {attributes[1].upper()}")
            i += 1
            for key in keys:
                print(f"{keys[j]} : {attributes[j]}")
                j += 1

    def select_player(i):
        print player_table[i]
