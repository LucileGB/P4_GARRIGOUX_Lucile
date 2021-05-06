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
kyoka = models.Player("Kyoka", "Isumi", "1991-01-31", "homme", 8)
clovis = models.Player("Clovis", "Premier", "1991-01-31", "homme", 3)
berthe = models.Player("Berthe", "Au grand pied", "1991-01-31", "femme", 5)

all_players = [dazai, megumi, chuuya, akutagawa, yuuji, nobara, atsushi,
               kyoka, clovis, berthe]

tournoitest = models.Tournament("Tournoi", "31 place des Marroniers",
                         "31/01/2021", "31/01/2021", "Bullet")

tournoitest.players = all_players

#test = controllers.MenuControl()
#test.naviguate_main()

tournoitest.new_round(all_players)

#for player in all_players:
#    player.table_insert_player()

#everything = models.Player.fetch_all_players()
#print(everything)
#test = models.Player.search_player("Clovis", "Premier")
#print(test)

#select = models.Player.select_player(3)

