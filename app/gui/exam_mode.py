import tkinter as tk

class ExamMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="lightcoral")
        
        # Crée les widgets de l'interface ExamMode
        self.create_widgets()

    def create_widgets(self):
        """Crée et place les widgets de l'interface ExamMode"""

        # Label pour le titre
        label = tk.Label(self, text="Mode examen", font=("Helvetica", 18), bg="lightcoral")
        label.pack(pady=20)

        # Bouton pour revenir en arrière
        back_button = tk.Button(self, text="Retour", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        """Retourne au menu principal"""
        self.switch_frame("MainMenu")
