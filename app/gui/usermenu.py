import tkinter as tk
from tkinter import simpledialog

class UserMenu(tk.Frame):
    """
    Correspond au menu des utilisateurs
    """
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        #couleurs relatives a la page
        self.bg_color = "#2B4162"        
        self.button_color = "#FA9F42"     
        self.title_color = "#871E1C"      
        self.text_color = "#F0BCC5"       
        self.highlight_color = "#0B6E4F"  

        self.configure(bg=self.bg_color)

        self.title_label = tk.Label(
            self, text="Voici la liste des Utilisateurs!", 
            font=("Montserrat", 22, "bold"), fg=self.title_color, bg=self.bg_color
        )
        self.title_label.pack(pady=20)

        self.back_button = tk.Button(
            self, text="Retour", command=self.go_back,
            font=("Montserrat", 14, "bold"), fg=self.text_color, bg=self.button_color,
            borderwidth=0, activebackground=self.highlight_color, activeforeground=self.text_color
        )
        self.back_button.pack(pady=10)

        self.adduser_button = tk.Button(
            self, text="Ajout Utilisateur", command=self.add_user,
            font=("Montserrat", 14, "bold"), fg=self.text_color, bg=self.button_color,
            borderwidth=0, activebackground=self.highlight_color, activeforeground=self.text_color
        )
        self.adduser_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("MainMenu")

    def add_user(self):
        pass
        
