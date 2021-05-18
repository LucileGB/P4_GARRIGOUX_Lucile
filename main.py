import controllers
import models
import views

chuuya = models.Player("Chuuya", "Nakahara", "31/01/1991", "homme", 1)
dazai = models.Player("Osamu", "Dazai", "31/01/1991", "homme", 1, 6)
yuuji = models.Player("Yuuji", "Itadori", "31/01/1991", "homme", 3)
megumi = models.Player("Megumi", "Fushiguro", "31/01/1991", "homme", 4)
nobara = models.Player("Nobara", "Kugisaki", "31/01/1991", "femme", 5)
atsushi = models.Player("Atsushi", "Nakajima", "31/01/1991", "homme", 6)
akutagawa = models.Player("Ryunosuke", "Akutagawa", "31/01/1991", "homme", 7)
kyoka = models.Player("Kyoka", "Isumi", "31/01/1991", "homme", 8)
clovis = models.Player("Clovis", "Premier", "31/01/1991", "homme", 3)
berthe = models.Player("Berthe", "Au grand pied", "31/01/1991", "femme", 5)

all_players = [dazai, megumi, chuuya, akutagawa, yuuji, nobara, atsushi,
               kyoka, clovis, berthe]

#tournoitest = models.Tournament("Tournoi", "31 place des Marroniers",
#                         "31/01/2021", "31/01/2021", "Bullet")
#tournoitest.players = all_players

#INITIALIZE DB
#for player in all_players:
#    player.table_insert_player()

#print(views.PlayerMenu.create_players())

#PLAYERS TEST
#controllers.PlayerControl.main_player_menu()

#MAIN_MENU test
controllers.MainControl.main()
#controllers.PlayerControl.create_player()
#views.PlayerMenu.create_player()

#controllers.PlayerControl.select_players()
#controllers.PlayerControl.main()
#models.Player.clear_participants()
