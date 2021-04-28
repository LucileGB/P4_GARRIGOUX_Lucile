import datetime
from datetime import date

import models

NB_PLAYERS = 8

class Checkforms:
    def __init__(self):
        pass

    def return_date(self, input):
        split_input = input.split("/")
        date = f"{split_input[2]}-{split_input[1]}-{split_input[0]}"
        return date

    def check_date(self, input):
        # Format birth date correctly and check its exists
        # IF BIRTH DATE BUGS, IT'S THAT LINE
        date = self.return_date(input)
        try:
            date.fromisoformat(date)
        except Exception:
            return False
        return True

    def check_names(self, name):
        for letter in name:
            if letter.isnumeric():
                return False
        return True

    def check_rank(self, rank):
        if rank.isnumeric() and rank > 0:
            return True
        else:
            return False

"""class GeneratePlayer:
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.first_name = first_name
        self.last_name = last_name"""

#nb players will be controlled by CONTROLLERS (8)

chuuya = models.Player("Chuuya", "Nakahara", "1991-01-31", "m", 1)
dazai = models.Player("Osamu", "Dazai", "1991-01-31", "m", 2)
yuuji = models.Player("Yuuji", "Itadori", "1991-01-31", "m", 3)
megumi = models.Player("Megumi", "Fushiguro", "1991-01-31", "m", 4)
nobara = models.Player("Nobara", "Kugisaki", "1991-01-31", "f", 5)
atsushi = models.Player("Atsushi", "Nakajima", "1991-01-31", "m", 6)
akutagawa = models.Player("Ryunosuke", "Akutagawa", "1991-01-31", "m", 7)
kyoka = models.Player("Kyoka", "Isumi", "1991-01-31", "f", 8)
