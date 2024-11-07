import tkinter as tk
from tkinter import simpledialog
from models.board import Leaderboard
from models.user import UserManager

class UserMenu(tk.Frame):
    def __init__(self, master, switch_frame, user_list=None):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.user_manager = UserManager(user_list or {})  # Initialise UserManager avec une liste d'utilisateurs par défaut

        # Styles et couleurs
        self.bg_color = "#2B4162"        
        self.button_color = "#FA9F42"     
        self.title_color = "#871E1C"      
        self.text_color = "#F0BCC5"       
        self.highlight_color = "#0B6E4F"  

        self.configure(bg=self.bg_color)

        self.title_label = tk.Label(
            self, text="Leaderboard des Utilisateurs", 
            font=("Montserrat", 22, "bold"), fg=self.title_color, bg=self.bg_color
        )
        self.title_label.pack(pady=20)

        self.back_button = tk.Button(
            self, text="Retour", command=self.go_back,
            font=("Montserrat", 14, "bold"), fg=self.text_color, bg=self.button_color,
            borderwidth=0, activebackground=self.highlight_color, activeforeground=self.text_color
        )
        self.back_button.pack(pady=10)

        self.add_user_button = tk.Button(
            self, text="Ajout Utilisateur", command=self.add_user,
            font=("Montserrat", 14, "bold"), fg=self.text_color, bg=self.button_color,
            borderwidth=0, activebackground=self.highlight_color, activeforeground=self.text_color
        )
        self.add_user_button.pack(pady=10)

        self.display_leaderboard()

    def go_back(self):
        self.switch_frame("MainMenu")

    def add_user(self):
        """
        Fonction pour ajouter un utilisateur via une boîte de dialogue.
        """
        name = simpledialog.askstring("Nom de l'utilisateur", "Entrez le nom de l'utilisateur:")
        
        if name:
            grades_str = simpledialog.askstring("Notes de l'utilisateur", "Entrez les notes séparées par des virgules:")
            try:
                grades = [int(g.strip()) for g in grades_str.split(",")]#convertit les g dans strip qui sont eux meme les valeurs rentré split strip nettoie les esoaces innutiles et convertit en int puis stocké dans grades
                self.user_manager.add_user(name)#Si les notes ont été correctement converties en entiers, la méthode add_user de user_manager est appelée pour ajouter un utilisateur avec le nom donné.
                for grade in grades:
                    self.user_manager.user_list[name].add_grade(grade)#ajoute chaque note a l'utilisteur dans le gestionnaire d'utilisateurs
                
                self.refresh_leaderboard()#met a jour le tableau
                
            except ValueError:#si il y a une erreur de Valeur:
                error_label = tk.Label(self, text="Erreur : Entrez des notes valides (nombres entiers séparés par des virgules).", 
                                       font=("Montserrat", 12), fg="red", bg=self.bg_color)
                error_label.pack()

    def refresh_leaderboard(self):
        """
        Met à jour l'affichage du leaderboard.
        """
        # Supprime les anciennes entrées du leaderboard
        for widget in self.winfo_children():#winfo_children prend tout les widgets enfant 
            if isinstance(widget, tk.Label) and widget not in [self.title_label, self.back_button, self.add_user_button]:#si le widget est un label et que le widget n'est pas la dans la liste[]
                widget.destroy()#alors on detruit les widgets

        self.display_leaderboard()

    def display_leaderboard(self):
        """
        Affiche le leaderboard trié.
        """
        leaderboard = Leaderboard(self.user_manager.get_user_list())  # Initialise Leaderboard
        leaderboard_data = leaderboard.refresh_board()  # Rafraîchir pour obtenir le leaderboard trié

        if leaderboard_data:
            for username, grades, avg in leaderboard_data:
                user_label = tk.Label(
                    self, text=f"{username}: Moyenne = {avg}, Notes = {grades}",
                    font=("Montserrat", 14), fg=self.text_color, bg=self.bg_color
                )
                user_label.pack()
        else:
            no_data_label = tk.Label(
                self, text="Aucune donnée de leaderboard disponible.",
                font=("Montserrat", 14), fg=self.text_color, bg=self.bg_color
            )
            no_data_label.pack()
