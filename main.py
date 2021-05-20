import controllers
import models
import views

chuuya = models.Player({"first_name": "Chuuya", "last_name": "Nakahara", "birth_date": "31/01/1991", "gender": "homme", "rank": 1, "score": 0, "is_playing": "False"})
dazai = models.Player({"first_name": "Osamu", "last_name": "Dazai", "birth_date": "31/01/1991", "gender": "homme", "rank": 1, "score": 0, "is_playing": "True"})
verlaine = models.Player({"first_name": "Paul", "last_name": "Verlaine", "birth_date": "31/01/1991", "gender": "homme", "rank": 3, "score": 0, "is_playing": "True"})
rimbault = models.Player({"first_name": "Arthur", "last_name": "Rimbault", "birth_date": "31/01/1991", "gender": "homme", "rank": 4, "score": 0, "is_playing": "True"})
alcott = models.Player({"first_name": "Louisa", "last_name": "Alcott", "birth_date": "31/01/1991", "gender": "femme", "rank": 5, "score": 0, "is_playing": "True"})
wells = models.Player({"first_name": "Orson", "last_name": "Wells", "birth_date": "31/01/1991", "gender": "homme", "rank": 6, "score": 0, "is_playing": "True"})
lovecraft = models.Player({"first_name": "Howard", "last_name": "Lovecraft", "birth_date": "31/01/1991", "gender": "homme", "rank": 7, "score": 0, "is_playing": "True"})
verne = models.Player({"first_name": "Jules", "last_name": "Verne", "birth_date": "31/01/1991", "gender": "homme", "rank": 8, "score": 0, "is_playing": "True"})
sand = models.Player({"first_name": "Georges", "last_name": "Sand", "birth_date": "31/01/1991", "gender": "femme", "rank": 3, "score": 0, "is_playing": "False"})
christie = models.Player({"first_name": "Agatha", "last_name": "Christie", "birth_date": "31/01/1991", "gender": "femme", "rank": 5, "score": 0, "is_playing": "True"})

all_players = [dazai, rimbault, chuuya, lovecraft, verlaine, alcott, wells,
               verne, sand, christie]

#INITIALIZE PLAYER DB
#for player in all_players:
#    player.table_insert_player()

#MAIN_MENU test
controllers.MainControl.main()
