import datetime
from tinydb import TinyDB, Query

NB_PLAYERS = 8
NB_ROUNDS = 4

db = TinyDB("db.json")
players_table = db.table("players")
tournament_table = db.table("tournaments")


class Player:
    def __init__(self, first_name=None, last_name=None,
                birth_date=None, gender=None,
                rank=0, score=0, is_playing = False):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.is_playing = is_playing

    def add_participant(self, i):
        list_players = players_table.all()
        participant = Player.instantiate_player(list_players[int(i)-1])
        return participant
        #set is_playing = True ??

    def serialize_player(self):
        serialized_player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "is_playing": self.is_playing,
        }
        return serialized_player

    def table_insert_player(self):
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
            attributes[6],
        )
        return result

    def show_all(self):
        i = 0
        serialized_players = players_table.all()
        for player in serialized_players:
            j = 0
            keys = ("Prénom", "Nom de famille", "Date de naissance",
                    "Genre", "Classement")
            attributes = list(player.values())
            print(f"\n{i+1}. {attributes[0].upper()} {attributes[1].upper()}")
            i += 1
            for key in keys:
                print(f"{keys[j]} : {attributes[j]}")
                j += 1

    def show_all_abridged(self):
        i = 0
        serialized_players = players_table.all()
        for player in serialized_players:
            attributes = list(player.values())
            print(f"\n{i+1}. {attributes[0].upper()} {attributes[1].upper()}")
            i += 1

    def alphabetical_list():
        players = players_table.all()
        players = sorted(players, key=lambda value: value["last_name"])
        return players

    def rank_list():
        players = players_table.all()
        players = sorted(players, key=lambda value: value["rank"])
        return players

    def final_ranking_list(tournament):
        participants = tournament.players
        players = sorted(players, key=lambda Player: Player.score)
        return players

    def instantiate_participants(list):
        new_list = []
        for participant in list:
            attributes = list(round.values())
            result = Player(attributes[0], attributes[1], attributes[2],
                    attributes[3], attributes[4], attributes[5], attributes[6])
            new_list += result
        return new_list

    def update_participant(self, first_name, last_name):
        Participant = Query()
        players_table.update({"rank": f"{self.rank}"},
                (Participant["first_name"] == first_name) &
                (Participant["last_name"] == last_name))
        players_table.update({"score": f"{self.score}"},
                (Participant["first_name"] == first_name) &
                (Participant["last_name"] == last_name))


class Match:
    def __init__(self, players=([], [])):
        self.players = players

    def set_result(self, winner):
        # 1 and 2 grant 1 points to the winner. 3 means a tie.
        if winner == 1:
            self.players[0][0].score += 1
            self.players[0][1] += 1
        elif winner == 2:
            self.players[1][0].score += 1
            self.players[1][1] += 1
        else:
            self.players[0][0].score += 0.5
            self.players[1][0].score += 0.5
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

    def serialize_round(self):
        serialized_round = {
            "Name": self.name,
            "Start": self.start,
            "End": self.end,
            "Matches": self.matches,
        }
        return serialized_round

    def instantiate_round(list):
        new_list = []
        for round in list:
            attributes = list(round.values())
            result = Round(attributes[0], attributes[1], attributes[2],
                    attributes[3])
            new_list += result
        return new_list

    def classify_list(self, list_players):
        list_players = sorted(list_players, key=lambda Player: Player.score)
        for player in list_players:
            for other_player in list_players:
                if (
                    player.score == other_player.score
                    and player.rank < other_player.rank
                ):
                    current_index = list_players.index(player)
                    new_index = list_players.index(other_player)
                    list_players.insert(new_index, player)
                    list_players.pop(current_index)
        return list_players

class Tournament:
    def __init__(
        self,
        name=None,
        place=None,
        date=None,
        end=None,
        time_control=None,
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

    def add_player(self, Player):
        self.players.append(Player)

    def serialize_tournament(self):
        list_rounds = []
        list_participants = []
        for round in self.rounds:
            result = round.serialize_round()
            list_rounds.append(result)
        for participant in self.players:
            result = participant.serialize_player()
            list_participants.append(result)

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
        rounds_list = []
        participants_list = []
        for round in attributes[7]:
            new_round = Round.instantiate_round(round)
            rounds_list.append(new_round)
        for participant in attributes[8]:
            new_participant = Player.instantiate_player(participant)
            participants_list.append(new_participant)

        result = Tournament(
            attributes[0],
            attributes[1],
            attributes[2],
            attributes[3],
            attributes[4],
            attributes[5],
            attributes[6],
            rounds_list,
            participants_list,
        )
        return result

    def return_last_tournament(self):
        list_tournaments = tournament_table.all()
        i = len(list_tournaments)
        tournament = self.instantiate_tournament(list_tournaments[int(i)-1])
        return tournament

    def serialize_tournament_rounds(self):
        Tournament = Query()
        date = self.date
        tournament_table.update({"date": f"{self.date}"},
                                Tournament["rounds"] == self.rounds)


    def new_round(self):
        nb_round = len(self.rounds) + 1
        past_matches = []
        higher_tier = []
        lower_tier = self.players.copy()
        i = 0
        j = 0

        for round_instance in self.rounds:
            past_matches += round_instance.matches

        round = Round(f"Round {nb_round}", f"{self.date}",
                    start=Round.time_now())
        self.rounds.append(round)
        lower_tier = round.classify_list(lower_tier)

        while len(higher_tier) < len(lower_tier):
            higher_tier.append(lower_tier[0])
            lower_tier.pop(0)

        while i + 1 <= len(higher_tier):
            match = (
                [higher_tier[i], higher_tier[i].score],
                [lower_tier[i], lower_tier[i].score],
            )
            for old_match in past_matches:
                if match[0][0] in old_match and match[0][1] in old_match:
                    match = (
                        [higher_tier[i], higher_tier[i].score],
                        [lower_tier[i + 1], lower_tier[i + 1].score],
                    )
            round.matches.append(match)
            i += 1
        self.serialize_tournament_rounds()

    def finish_round(self):
        list_rounds = []
        list_participants = []
        i = 0
        Tournament = Query()
        for round in self.rounds:
            if i == len(self.rounds)- 1:
                round.end = f"{Round.time_now()}"
                for match in round.matches:
                    match[0][0] = match[0][0].serialize_player()
                    match[1][0] = match[1][0].serialize_player()
            result = round.serialize_round()
            list_rounds.append(result)
            i += 1
            print(result)
        tournament_table.update({"date": f"{self.date}"},
                                Tournament["rounds"] == list_rounds)
        for round in self.rounds:
            for match in round.matches:
                match[0][0] = Player.instantiate_player(match[0][0])
                match[1][0] = Player.instantiate_player(match[1][0])
