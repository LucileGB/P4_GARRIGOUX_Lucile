import controllers
import models
import views

chuuya = models.Player("Chuuya", "Nakahara", "31/01/1991", "homme", 1)
dazai = models.Player("Osamu", "Dazai", "31/01/1991", "homme", 1, 6)
verlaine = models.Player("Paul", "Verlaine", "31/01/1991", "homme", 3)
rimbault = models.Player("Arthur", "Rimbault", "31/01/1991", "homme", 4)
alcott = models.Player("Louisa", "Alcott", "31/01/1991", "femme", 5)
wells = models.Player("Orson", "Wells", "31/01/1991", "homme", 6)
akutagawa = models.Player("Howard", "Lovecraft", "31/01/1991", "homme", 7)
verne = models.Player("Jules", "Verne", "31/01/1991", "homme", 8)
sand = models.Player("Georges", "Sand", "31/01/1991", "femme", 3)
christie = models.Player("Agatha", "Christie", "31/01/1991", "femme", 5)

all_players = [dazai, rimbault, chuuya, akutagawa, verlaine, alcott, wells,
               verne, sand, christie]

#INITIALIZE PLAYER DB
#for player in all_players:
#    player.table_insert_player()

#MAIN_MENU test
controllers.MainControl.main()
