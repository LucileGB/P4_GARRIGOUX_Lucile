#nb players will be controlled by CONTROLLERS (8)
#rank = positive (CONTROLLERS)
NB_ROUNDS = 4


class Tournoi:
    def __init__(self, name, place, date, end, time_control,
                description, nb_rounds=NB_ROUNDS, rounds=[], players=[]
                ):
        #Duration is 1 for a one-day tournament. It's set by default since
        #tournaments last one day for now.
        self.name = name
        self.place = place
        self.date = date
        self.end = end
        #bullet, blitz, coup rapide??
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.players = players


class Player:
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank


class Round:
    def __init__(self, name, start, end, matches=[]):
        self.name = name
        self.stat = start
        self.end = end
        self.matches = matches


class Match:
    def __init__(self, players = {}):
        self.players = players
        #Dictionary: name:, score:
