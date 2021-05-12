import controllers
import models
import views

chuuya = models.Player("Chuuya", "Nakahara", "1991-01-31", "homme", 1)
dazai = models.Player("Osamu", "Dazai", "1991-01-31", "homme", 1, 6)
yuuji = models.Player("Yuuji", "Itadori", "1991-01-31", "homme", 3)
megumi = models.Player("Megumi", "Fushiguro", "1991-01-31", "homme", 4)
nobara = models.Player("Nobara", "Kugisaki", "1991-01-31", "femme", 5)
atsushi = models.Player("Atsushi", "Nakajima", "1991-01-31", "homme", 6)
akutagawa = models.Player("Ryunosuke", "Akutagawa", "1991-01-31", "homme", 7)
kyoka = models.Player("Kyoka", "Isumi", "1991-01-31", "homme", 8)
clovis = models.Player("Clovis", "Premier", "1991-01-31", "homme", 3)
berthe = models.Player("Berthe", "Au grand pied", "1991-01-31", "femme", 5)

all_players = [dazai, megumi, chuuya, akutagawa, yuuji, nobara, atsushi,
               kyoka, clovis, berthe]

#tournoitest = models.Tournament("Tournoi", "31 place des Marroniers",
#                         "31/01/2021", "31/01/2021", "Bullet")
#tournoitest.players = all_players

#INITIALIZE DB
#for player in all_players:
#    player.table_insert_player()

#PLAYERS TEST
"""test = controllers.PlayerControl()
main = test.main_player_menu()"""

#MAIN_MENU test
test = controllers.MainControl()
test = test.main()
