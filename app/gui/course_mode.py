import tkinter as tk
from PIL import Image, ImageTk

class CoursMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        self.bg_color = "#2B4162"         
        self.button_color = "#FA9F42"    
        self.title_color = "#871E1C"      
        self.text_color = "#F0BCC5"       
        self.highlight_color = "#0B6E4F"  

        self.configure(bg=self.bg_color)

        self.create_widgets()

        self.show_view()

    def create_widgets(self):
        """Crée et configure les widgets de l'interface CoursMode"""

        self.label = tk.Label(
            self, text="Mode Cours", font=("Montserrat", 24, "bold"), 
            fg=self.title_color, bg=self.bg_color
        )
        
        self.back_button = tk.Button(
            self, text="Retour", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

    def show_view(self):
        """Affiche la vue principale de CoursMode"""
        self.label.pack(pady=20)
        self.back_button.pack(pady=10)

    def go_back(self):
        """Retourne au menu principal"""
        self.switch_frame("MainMenu")
