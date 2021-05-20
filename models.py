import datetime
from tinydb import TinyDB, Query

NB_PLAYERS = 8
NB_ROUNDS = 4

db = TinyDB("db.json")
players_table = db.table("players")
tournament_table = db.table("tournaments")


class Player:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        birth_date=None,
        gender=None,
        rank=0,
        score=0,
        is_playing="False",
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.is_playing = is_playing

    def has_double(self):
        Player = Query()
        result = players_table.search(
            (Player.first_name == f"{self.first_name}")
            & (Player.last_name == f"{self.last_name}")
            & (Player.birth_date == f"{self.birth_date}")
        )
        if len(result) == 0:
            return False
        else:
            return True

    def save(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "is_playing": self.is_playing,
        }

    def table_insert_player(self):
        player = self.save()
        players_table.insert(player)

    def update_participant(self):
        Participant = Query()
        players_table.update({"score": self.score},
                (Participant["first_name"] == self.first_name)
                & (Participant["last_name"] == self.last_name)
                & (Participant["birth_date"] == self.birth_date),
            )
        players_table.update({"rank": self.rank},
                (Participant["first_name"] == self.first_name)
                & (Participant["last_name"] == self.last_name)
                & (Participant["birth_date"] == self.birth_date),
            )

    @staticmethod
    def all():
        serialized_players = players_table.all()
        return serialized_players

    @staticmethod
    def change_rank(first_name, last_name, birth_date, new_value):
        Participant = Query()
        players_table.update(
            {"rank": new_value},
            (Participant["first_name"] == first_name)
            & (Participant["last_name"] == last_name)
            & (Participant["birth_date"] == birth_date),
        )
    @staticmethod
    def clear_participants():
        players_table.update({"is_playing": "False"})
        players_table.update({"score": 0})

    @staticmethod
    def instantiate(player_dict):
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

    @staticmethod
    def is_playing_true(first_name, last_name, birth_date):
        Participant = Query()
        players_table.update(
            {"is_playing": "True"},
            (Participant["first_name"] == first_name)
            & (Participant["last_name"] == last_name)
            & (Participant["birth_date"] == birth_date),
        )

    @staticmethod
    def list_abridged(list_to_abridge):
        """Print an alphabetical, more lisible version of a player list,
        showing only each player's complete name and birthdate. Also return
        the alphabetically sorted list."""
        i = 0
        abridged_list = Player.alphabetical_list(list_to_abridge)
        for player in abridged_list:
            attributes = list(player.values())
            print(f"\n{i+1}. {attributes[0]} {attributes[1].upper()}")
            print(f"{attributes[2]}")
            i += 1
        return abridged_list

    @staticmethod
    def list_not_participants():
        Player = Query()
        result = players_table.search(Player.is_playing == "False")
        return result

    @staticmethod
    def list_participants():
        Player = Query()
        result = players_table.search(Player.is_playing == "True")
        return result

    @staticmethod
    def show_all(serialized_player):
        """Show all attributes of all players."""
        i = 0
        for player in serialized_players:
            j = 0
            keys = (
                "Prénom",
                "Nom de famille",
                "Date de naissance",
                "Genre",
                "Classement",
            )
            attributes = list(player.values())
            print(f"\n{i+1}. {attributes[0].upper()} {attributes[1].upper()}")
            i += 1
            for key in keys:
                print(f"{keys[j]} : {attributes[j]}")
                j += 1

    @staticmethod
    def alphabetical_list(unsorted):
        return sorted(unsorted, key=lambda value: value["last_name"])

    @staticmethod
    def rank_list():
        players = players_table.all()
        return sorted(players, key=lambda value: value["rank"],
                        reverse = True)

    @staticmethod
    def final_ranking_list(tournament):
        participants = tournament.players
        players = sorted(players, key=lambda Player: Player.score,
                        reverse = True)
        return players

class Match:
    def __init__(self, match=([], [])):
        self.match = match

    def set_result(self, winner):
        """1 and 2 grant 1 points to the winner. 3 means a tie."""
        if winner == 1:
            self.match[0][0].score += 1
            self.match[0][0].rank += 1
            self.match[0][1] += 1
        elif winner == 2:
            self.match[1][0].score += 1
            self.match[1][0].rank += 1
            self.match[1][1] += 1
        else:
            self.match[0][0].score += 0.5
            self.match[0][0].rank += 0.5
            self.match[0][1] += 0.5
            self.match[1][0].score += 0.5
            self.match[1][0].rank += 0.5
            self.match[1][1] += 0.5

        return self.match

    def serialize_match(self):
        self.match[0][0] = self.match[0][0].save()
        self.match[1][0] = self.match[1][0].save()
        return self.match

    @staticmethod
    def instantiate_match(match):
        match[0][0] = Player.instantiate(match[0][0])
        match[1][0] = Player.instantiate(match[1][0])
        return match

    @staticmethod
    def compare(new_match, past_match):
        #Once deployed, function to compare new_match[0]etc name, name, birth_date
        if new_match[0][0] == past_match[0][0] or new_match[0][0] == past_match[1][0]:
            if new_match[1][0] == past_match[0][0] or new_match[1][0] == past_match[1][0]:
                return True

    @staticmethod
    def match_sorting(new_matches, past_matches):
        """Use Match.compare to check whether two players have already
        played together. If so, player1 plays with player3, etc.
        If it's the last match, the algorythm change to ensure no repetition."""
        i = 0
        for new_match in new_matches:
            for past_match in past_matches:
                if compare(new_match, past_match) == True:
                    if i == len(new_matches)-1:
                        pair_one = ([new_matches[i][0][0], new_matches[i][0][1]],
                                     [new_matches[i-1][0][0], new_matches[i-1][0][1]])
                        pair_two = ([new_matches[i][1][0], new_matches[i][1][1]],
                                     [new_matches[i-1][1][0], new_matches[i-1][1][1]])
                        new_matches[i] = pair_one
                        new_matches[i-1] = pair_two
                    else:
                        pair_one = ([new_matches[i][0][0], new_matches[i][0][1]],
                                     [new_matches[i+1][0][0], new_matches[i+1][0][1]])
                        pair_two = ([new_matches[i][1][0], new_matches[i][1][1]],
                                     [new_matches[i+1][1][0], new_matches[i+1][1][1]])
                        new_matches[i] = pair_one
                        new_matches[i+1] = pair_two
            i += 1

class Round:
    def __init__(self, name, start=None, end=None, matches=[]):
        self.name = name
        self.start = start
        self.end = end
        self.matches = matches

    @staticmethod
    def instantiate(list_rounds):
        list_instances = []

        for dictionary in list_rounds:
            attributes = list(dictionary.values())
            for match in attributes[3]:
                match = Match.instantiate_match(match)
            result = Round(attributes[0], attributes[1], attributes[2], attributes[3])
            list_instances.append(result)
        return list_instances

    @staticmethod
    def sort_players(list_players):
        list_players = list(reversed(
            sorted(list_players, key=lambda Player: (Player.score, Player.rank))
        ))
        return list_players

    @staticmethod
    def time_now():
        beginning = datetime.datetime.now()
        beginning = beginning.strftime("%d/%m/%Y à %H:%M")
        return beginning

    def serialize_round(self):
        for match in self.matches:
            match_to_serialize = Match(match)
            match = match_to_serialize.serialize_match()

        serialized_round = {
            "Name": self.name,
            "Start": self.start,
            "End": self.end,
            "Matches": self.matches,
        }
        return serialized_round


class Tournament:
    def __init__(
        self,
        name=None,
        place=None,
        date=None,
        duration=None,
        time_control=None,
        description=None,
        nb_rounds=NB_ROUNDS,
        rounds=[],
        players=[],
        ended=None
    ):
        self.name = name
        self.place = place
        self.date = date
        self.duration = duration
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.players = players
        self.ended = None

    @staticmethod
    def all_tournaments():
        list_tournament = tournament_table.all()
        return list_tournament

    @staticmethod
    def instantiate_tournament(tournament_dict):
        attributes = list(tournament_dict.values())
        participants_list = []
        rounds_list = Round.instantiate(attributes[7])

        for participant in attributes[8]:
            new_participant = Player.instantiate(participant)
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
            attributes[9]
        )
        return result

    @staticmethod
    def return_last_tournament():
        list_tournaments = tournament_table.all()
        last_tournament = Tournament.instantiate_tournament(
            list_tournaments[-1]
        )
        return last_tournament

    def add_player(self, Player):
        self.players.append(Player)

    def round_start(self):
        nb_round = len(self.rounds) + 1
        past_matches = []

        if len(self.rounds) == 0:
            higher_tier = []
            lower_tier = self.players.copy()
            i = 0

            new_round = Round(f"Tour {nb_round}", start=Round.time_now())
            self.rounds.append(new_round)
            lower_tier = new_round.sort_players(lower_tier)

            while len(higher_tier) < len(lower_tier):
                higher_tier.append(lower_tier[0])
                lower_tier.pop(0)

            while i + 1 <= len(higher_tier):
                match = (
                    [higher_tier[i], higher_tier[i].score],
                    [lower_tier[i], lower_tier[i].score],
                )
                new_round.matches.append(match)
                i += 1

        else:
            to_sort = self.players.copy()
            print(len(self.players))
            sorted = Round.sort_players(to_sort)
            i = 0

            new_round = Round(f"Tour {nb_round}", start=Round.time_now())
            list_matches = []
            print("LONGUEUR MATCHES (pré-ajout)")
            print(f"{new_round.matches}")
            for i in range(0, 7, 2):
                match_to_add = (
                    [sorted[i], sorted[i].score],
                    [sorted[i+1], sorted[i+1].score]
                )

                new_round.matches.append(match_to_add)
            print("LONGUEUR MATCH (post-ajout)")
            print(new_round.matches)
            self.rounds.append(new_round)

    def round_end(self, results):
        current_round = self.rounds[-1]
        list_rounds = []
        list_participants = []
        Tournament = Query()
        i = 0

        current_round.end = f"{Round.time_now()}"

        for match in current_round.matches:
            match_instance = Match(match)
            outcome = match_instance.set_result(int(results[i]))
            match = outcome
            i += 1

        for player in self.players:
            player.update_participant()

        self.round_update()

        for match in current_round.matches:
            match = Match.instantiate_match(match)

    def round_update(self):
        Tournament = Query()
        rounds_to_serialize = self.rounds.copy()
        rounds_serialized = []
        players_to_serialize = self.players.copy()
        players_serialized = []
        i = 0
        j = 1

        for round_instance in self.rounds:
            print(f"ROUND {j}\n")
            print(round_instance.matches)
            j += 1

        for round_instance in rounds_to_serialize:
            print(round_instance.matches)
            print(i)
            round_instance = round_instance.serialize_round()
            rounds_serialized.append(round_instance)
            i += 1

        for player in players_to_serialize:
            player = Player.save(player)
            players_serialized.append(player)

        tournament_table.update(
            {"Rounds": rounds_serialized}, (Tournament["Date"] == self.date)
        )
        tournament_table.update(
            {"Participants": players_serialized}, (Tournament["Date"] == self.date)
        )


    def save(self):
        list_rounds = []
        list_participants = []
        for round in self.rounds:
            result = round.serialize_round()
            list_rounds.append(result)
        for participant in self.players:
            result = participant.save()
            list_participants.append(result)

        serialized_tournament = {
            "Nom": self.name,
            "Lieu": self.place,
            "Date": self.date,
            "Duree": self.duration,
            "Gestion temps": self.time_control,
            "Description": self.description,
            "Nombre de rounds": self.nb_rounds,
            "Rounds": list_rounds,
            "Participants": list_participants,
            "Fini": self.ended
        }
        tournament_table.insert(serialized_tournament)

    def ended(self):
        tournament_table.update(
            {"Fini": "True"}, (Tournament["Date"] == self.date)
        )
