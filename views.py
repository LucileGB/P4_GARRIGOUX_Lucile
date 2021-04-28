#Container code by Bryan Oakley.
import tkinter as tk
from tkinter import font as tkfont



class ChessApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Gestionnaire de tournois d'échecs")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartMenu, CreateTournament, AddPlayers, CreatePlayers,
                TournamentRound, TournamentEnded, RapportsFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartMenu")

        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Modifier un classement",
                            command=lambda: self.show_frame("CreatePlayers"))
        file_menu.add_command(label="Rapports",
                            command=lambda: self.show_frame("CreateTournament"))
        file_menu.add_command(label="Quitter", command=self.destroy)
        menubar.add_cascade(label="Plus d'options", menu=file_menu)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = tk.Frame(self)
        button_frame = tk.Frame(self)


        title_main = tk.Label(title_frame, text = "Menu principal",
                            font=controller.title_font)
        new_tournament = tk.Button(button_frame, text="Créer un nouveau tournoi",
                            command=lambda: controller.show_frame("CreateTournament"))
        load_tournament = tk.Button(button_frame, text="Reprendre le tournoi actuel",
                            command=lambda: controller.show_frame("Tournament"))

        title_frame.grid(columnspan=5)
        button_frame.grid(row=1, columnspan=5)
        title_main.grid(row=0, column=2, pady=15)
        new_tournament.grid(row=0, column=1, pady=10, padx=10)
        load_tournament.grid(row=0, column=3, pady=10, padx=10)


class CreateTournament(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = tk.Frame(self)
        top_frame = tk.Frame(self)
        middle_frame = tk.Frame(self)
        bottom_frame = tk.Frame(self)

        title_frame.grid(columnspan=4)
        top_frame.grid(row=1, columnspan=4)
        middle_frame.grid(row=2, columnspan=3)
        bottom_frame.grid(row=3, columnspan=3)

        title_tournament = tk.Label(title_frame, text="Créer un tournoi",
                        font=controller.title_font)
        name = tk.Label(top_frame, text="Nom")
        place = tk.Label(top_frame, text="Lieu")
        date = tk.Label(top_frame, text="Date")
        end_date = tk.Label(top_frame, text="Date de fin")
        name_field = tk.Text(top_frame, height=3, width=20)
        place_field = tk.Text(top_frame, height=3, width=25)
        date_field = tk.Entry(top_frame)
        end_date_field = tk.Entry(top_frame)
        date_field.insert(0, "Format: 31/01/2001")
        end_date_field.insert(0, "Format: 31/01/2001")

        nb_tour = tk.Label(middle_frame, text="Nombre de tours")
        time_control = tk.Label(middle_frame, text="Contrôle du temps")
        nb_tour_field = tk.Entry(middle_frame)
#Do not forget to change once you're sure (+listbox)
        time_control_choice = tk.Listbox(middle_frame, height=1)
        nb_tour_field.insert(0, "4")

        description = tk.Label(bottom_frame, text="Remarques générales")
        description_field = tk.Text(bottom_frame, height=10, width=40)
        player_input = tk.Button(bottom_frame, text="Ajouter des joueurs",
                    command=lambda: controller.show_frame("CreatePlayers"))

        title_tournament.grid(column=1, columnspan=2, pady=15)
        name.grid(row=0, pady=5)
        place.grid(row=0, column = 1, pady=5)
        date.grid(row=2, column=0, pady=5)
        end_date.grid(row=2, column=1, pady=5)
        name_field.grid(row=1, pady=5)
        place_field.grid(row=1, column=1, pady=5)
        date_field.grid(row=3, column=0, pady=5)
        end_date_field.grid(row=3, column=1, pady=5)

        nb_tour.grid(row=0, column=0, pady=5)
        time_control.grid(row=0, column=1, pady=5)
        nb_tour_field.grid(row=1, column=0, pady=5)
        time_control_choice.grid(row=1, column=1, pady=5)

        description.grid(row=0, column=1, pady=8, padx=10)
        description_field.grid(row=1, columnspan=3, pady=5, padx=5)
        player_input.grid(row=2, column=1, pady=15)

class AddPlayers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = tk.Frame(self)
        top_frame = tk.Frame(self)
        middle_frame = tk.Frame(self)
        bottom_frame = tk.Frame(self)

        title_frame.grid(columnspan=3)
        top_frame.grid(row=1, columnspan=4)
        middle_frame.grid(row=2, columnspan=3)
        bottom_frame.grid(row=3, columnspan=3)

        title_tournament = tk.Label(title_frame, text="Ajouter des joueurs",
                        font=controller.title_font)
        create_player = tk.Button(title_frame, text="Créer un joueur",
                        command=lambda: self.show_frame("CreateTournament"))

        okay_button = tk.Button(bottom_frame, text="Valider",
                        command=lambda: self.show_frame("CreateTournament"))

        title_tournament.grid(column=1, pady=15)
        create_player.grid(row=1, column=1, pady=10)
        okay_button.grid(column=1, pady=10)

class CreatePlayers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = tk.Frame(self)
        top_frame = tk.Frame(self)
        middle_frame = tk.Frame(self)
        bottom_frame = tk.Frame(self)

        title_frame.grid(columnspan=3)
        top_frame.grid(row=1, columnspan=3)
        middle_frame.grid(row=2, columnspan=4)
        bottom_frame.grid(row=3, columnspan=3)

        first_name_value = tk.StringVar()
        last_name_value = tk.StringVar()
        birth_date_value = tk.StringVar()
        #gender_field = how to make return value?
        rank_value = tk.StringVar()

        title_player_create = tk.Label(title_frame, text="Créer des joueurs",
                        font=controller.title_font)
        first_name = tk.Label(top_frame, text="Prénom")
        last_name = tk.Label(top_frame, text="Nom de famille")
        birth_date = tk.Label(top_frame, text="Date de naissance")
        first_name_field = tk.Entry(top_frame, textvariable=first_name_value)
        last_name_field = tk.Entry(top_frame, textvariable=last_name_value)
        birth_date_field = tk.Entry(top_frame, textvariable=birth_date_value)
        birth_date_field.insert(0, "Format: 31/01/2001")

        gender = tk.Label(middle_frame, text="Genre")
        rank = tk.Label(middle_frame, text="Classement")
        gender_field = tk.Listbox(middle_frame, height=2)
        rank_field = tk.Entry(middle_frame, textvariable=rank_value)

        okay_button = tk.Button(bottom_frame, text="Valider",
                        command=lambda: self.show_frame("CreateTournament"))

        title_player_create.grid(column=1)
        first_name.grid(row=0, column=0, padx=5)
        last_name.grid(row=0, column=1, padx=5)
        birth_date.grid(row=0, column=2, padx=5)
        first_name_field.grid(row=1, column=0, padx=5)
        last_name_field.grid(row=1, column=1, padx=5)
        birth_date_field.grid(row=1, column=2, padx=5)

        gender.grid(row=0, column=0, padx=5)
        rank.grid(row=0, column=1, padx=5)
        gender_field.grid(row=1, column=0, padx=5)
        rank_field.grid(row=1, column=1, padx=5)

        okay_button.grid(column=1, pady=10)

class TournamentRound(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

class TournamentEnded(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

class RapportsFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

#Fenêtres additionnelles: modifier classement, rapport_window
