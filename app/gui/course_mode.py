import tkinter as tk
from PIL import Image, ImageTk

class CoursMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="lightgreen")
        self.create_widgets()
        
        self.show_view()

    def create_widgets(self):
        """Crée et configure les widgets de l'interface CoursMode"""

        # Titre du mode Cours
        self.label = tk.Label(self, text="Mode Cours", font=("Montserrat", 18), bg="lightgreen")
       
        self.back_button = tk.Button(self, text="Retour", command=self.go_back)

    def show_view(self):
        """Affiche la vue principale de CoursMode"""
        self.label.pack(pady=20)
        self.back_button.pack(pady=10)

    def go_back(self):
        """Retourne au menu principal"""
        self.switch_frame("MainMenu")
