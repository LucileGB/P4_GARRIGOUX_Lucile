import gettext

gettext.install("P4", "/locale")

# Unifier mention R


class Texts:
    main_menu = _("""                            ***
                    ~ MENU PRINCIPAL ~
                            ***\n
Veuillez taper la lettre correspondant au menu désiré :\n
N. Créer un nouveau tournoi ;
C. Continuer un tournoi en cours ;
R. Consulter les rapports (classements de joueurs, tournois passés...) ;
U. Changer directement les classements des joueurs ;\n
A tout moment, vous pouvez quitter le programme en tapant Q.
    """)

    menu_tournament = """CREATION DE TOURNOI\n
Pour revenir à l'écran d'accueil, tapez R.

Pour créer un tournoi, veuillez taper les informations suivantes :\n"""
    menu_players = """Bienvenue dans le menu d'ajout de joueurs.

1. Sélectionner des joueurs existants
2. Créer un nouveau joueur.\n"""

    ranking_rounds = """\nVeuillez taper le caractère correspondant à l'option souhaitée.
R. Retour au menu principal\n"""

    menu_change_ranks = """
Sélectionnez un joueur en tapant le numéro associé, puis tapez son nouveau rang.
Vous pouvez retourner sur l'écran d'accueil en tapant R.\n"""

    menu_create_player = """CREATION DE JOUEUR\n
Pour retourner au menu Joueurs, tapez R.

Pour créer un joueurs, veuillez taper les informations suivantes :\n"""
    new_gender = """Veuillez entrer un genre : homme ou femme.\n"""
    wrong_date = """Date invalide. Format : jour/mois/année.
Merci d'entrer une date conforme.\n"""
    wrong_time_control = """Veuillez taper le chiffre correspondant à votre sélection :
1. Bullet
2. Blitz
3. Coup rapide\n"""

    select_players = """Pour sélectionner un joueur, entrez le chiffre correspondant.\n"""

    new_rank = """Veuillez taper le nouveau nombre de point. S'il y a une décimale, utilisez un point à la place d'une virgule (ex : 10.5).
Pour retourner au menu précédent, tapez R.\n"""

    matches_instructions = """Entrer les résultats :
1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné, 3 pour un match nul.\n"""

    end_menu = """\nVeuillez entrer le caractère correspondant à la sélection souhaitée.
1. Retour à l'écran d'accueil
Q. Quitter\n"""

    confirm_choice = "Confirmez votre choix (o/n) :"

class TextsRanking:
    main = """RAPPORTS\n
1. Liste de tous les joueurs
2. Liste de tous les tournois\n"""

    players = """RAPPORTS : JOUEURS\n
A. Liste par ordre alphabétique
S. Liste par score total\n
"""

    players_sorted = """
A. Liste par ordre alphabétique
S. Liste par score total
R. Retour\n
"""
    tournaments_list = """\nPour sélectionner un tournoi, tapez le chiffre correspondant.
Pour revenir à l'écran Rapport, tapez R.\n"""

    tournament = """\nVeuillez entrer le caractère correspondant à l'option souhaitée.
A. Liste des joueurs par ordre alphabétique
S. Liste des joueurs par classement
D. Liste des tours et matches du tournoi
R. Retour à l'écran rapport\n"""

    rounds = """\nTapez R pour retourner à l'écran du tournoi\n"""

class TextsModels:
    tournament_form = [
        "Nom :",
        "Adresse :",
        "Date :",
        "Durée (en jours) :",
        "Contrôle de temps :",
        "Notes ou description :",
    ]

    player_form = [
        "Prénom : ",
        "Nom de famille : ",
        "Date de naissance (format : jour/mois/année) : ",
        "Genre (homme/femme): ",
        "Classement (nombre total de points): ",
    ]
