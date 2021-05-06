import datetime
from tinydb import TinyDB, Query

NB_PLAYERS = 8
NB_ROUNDS = 4

db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")


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

    def serialize_round():
        serialized_round = {
            "Name": self.name,
            "Start": self.start,
            "End": self.end,
            "Matches": self.matches,
        }
        return serialized_round

    def instantiate_rounds(list):
        new_list = []
        for round in list:
            attributes = list(round.values())
            result = Round(attributes[0], attributes[1], attributes[2],
                    attributes[3])
            new_list += result
        return new_list

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

    def serialize_tournament(self):
        list_rounds = []
        list_participants = []
        for round in self.rounds:
            result = round.serialize_round()
            list_rounds = list_rounds.append(result)
        for participant in self.players:
            result = participant.serialize_player()
            list_participants = list_participants.append(result)

        serialized_tournament = {
            "Nom": self.name,
            "Lieu": self.place,
            "Date": self.date,
            "Fin": self.end,
            "Gestion temps": self.time_control,
            "Description": self.description,
            "Nombre de rounds": self.nb_rounds,
            "Rounds": list_rounds,
            "Participants": list_participants
        }
        tournament_table.insert(serialized_tournament)

    def instantiate_tournament(self, tournament_dict):
        attributes = list(tournament_dict.values())
        round_list = Round.instantiate_rounds(attributes[7])
        participants_list = Player.instantiate_players(attributes[8])
        result = Player(
            attributes[0],
            attributes[1],
            attributes[2],
            attributes[3],
            attributes[4],
            attributes[5],
            attributes[6],
            round_list,
            participants_list,
        )
        return result

    def new_round(self, player_list):
        nb_round = len(self.rounds) + 1
        past_matches = []
        higher_tier = []
        i = 0

        for round_instance in self.rounds:
            past_matches += round_instance.matches

        round = Round(f"Round {nb_round}", f"{self.date}",
                    start=Round.time_now())
        self.rounds.append(round)

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
            round.matches.append(match)
            i += 1
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
        serialized_player = {
            "Prenom": self.first_name,
            "Nom": self.last_name,
            "Date de naissance": self.birth_date,
            "Genre": self.gender,
            "Classement": self.rank,
            "Score": self.score,
        }
        return serialized_player

    def table_insert_player(self, player):
        player = self.serialize_player()
        players_table.insert(player)

    def instantiate_player(player_dict):
        attributes = list(player_dict.values())
        result = Player(
            attributes[0],
            attributes[1],
            attributes[2],
            attributes[3],
            attributes[4],
            attributes[5],
        )
        return result

    def instantiate_participants(list):
        new_list = []
        for participant in list:
            attributes = list(round.values())
            result = Player(attributes[0], attributes[1], attributes[2],
                    attributes[3], attributes[4], attributes[5])
            new_list += result
        return new_list

    def search_player(first_name, last_name):
        Players = Query()
        result = players_table.search(
            Players.Prenom == first_name and Players.Nom == last_name
        )
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

    def select_player(number):
        i = 1
        for player in players_table:
            if i == number:
                print(player)
            i += 1
