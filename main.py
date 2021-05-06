import controllers
import models
import views

chuuya = models.Player("Chuuya", "Nakahara", "1991-01-31", "homme", 1)
dazai = models.Player("Osamu", "Dazai", "1991-01-31", "homme", 2)
yuuji = models.Player("Yuuji", "Itadori", "1991-01-31", "homme", 3)
megumi = models.Player("Megumi", "Fushiguro", "1991-01-31", "homme", 4)
nobara = models.Player("Nobara", "Kugisaki", "1991-01-31", "femme", 5)
atsushi = models.Player("Atsushi", "Nakajima", "1991-01-31", "homme", 6)
akutagawa = models.Player("Ryunosuke", "Akutagawa", "1991-01-31", "homme", 7)
kyoka = models.Player("Kyoka", "Isumi", "1991-01-31", "femme", 8)

all_players = [dazai, megumi, chuuya, akutagawa, yuuji, nobara, atsushi, kyoka]

tournoitest = models.Tournament("Tournoi", "31 place des Marroniers",
                         "31/01/2021", "31/01/2021", "time_control")

tournoitest.players = all_players

dp = models.Match((["Chuuya", 0], ["Dazai", 0]))
dp.set_result(3)


test = controllers.MenuControl()
test.naviguate_main()
#tournoitest.new_round(all_players)
