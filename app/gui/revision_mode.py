import tkinter as tk
from PIL import Image, ImageTk

from app.models.question import Question


class RevisionMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        # Crée les widgets de l'interface
        self.create_widgets()

        # Affiche l'interface initiale
        self.show_initial_view()

        question = Question("rrr", ("ah", "r"), ("ah"), "OOP", "e", True)
        question.start(self, 2)

    def create_widgets(self):
        """Crée et configure les widgets de l'interface RevisionMode"""

        # Configuration de base
        self.configure(bg="lightblue")

        # Titre du mode Révision
        self.title_label = tk.Label(self, text="Mode Révision", font=("Montserrat", 18), bg="lightblue")

        # Image de début pour le bouton
        image_path = "app\\assets\\images\\"
        self.revision_image = Image.open(image_path + "classement.png")
        self.revision_image = self.revision_image.resize((100, 100))
        self.revision_image = ImageTk.PhotoImage(self.revision_image)

        # Boutons pour l'interface initiale
        self.enter_button = tk.Button(self, image=self.revision_image, command=self.show_revision_view, borderwidth=0)
        self.back_button = tk.Button(self, text="Retour", command=self.go_back)

        # Widgets pour la vue de révision
        self.new_content_label = tk.Label(self, text="Bienvenue dans la révision !", font=("Montserrat", 18), bg="lightgreen")
        self.back_to_main_button = tk.Button(self, text="Retour au menu principal", command=self.go_back)

    def show_initial_view(self):
        """Affiche la vue initiale du mode révision."""
        self.configure(bg="lightblue")

        # Affiche les widgets de l'interface initiale
        self.title_label.pack(pady=20)
        self.enter_button.pack(pady=10)
        self.back_button.pack(pady=10)

    def show_revision_view(self):
        """Affiche la vue de révision en masquant l'interface initiale."""
        # Masque les widgets de l'interface initiale
        self.title_label.pack_forget()
        self.enter_button.pack_forget()
        self.back_button.pack_forget()

        # Change l'arrière-plan et affiche les widgets de la nouvelle interface
        self.configure(bg="lightgreen")
        self.new_content_label.pack(pady=20)
        self.back_to_main_button.pack(pady=10)

    def go_back(self):
        """Retourne au menu principal ou à la vue initiale du mode révision."""
        # Masque les widgets de la vue de révision
        self.new_content_label.pack_forget()
        self.back_to_main_button.pack_forget()

        # Réaffiche l'interface initiale
        self.show_initial_view()

        # Retourne au menu principal
        self.switch_frame("MainMenu")
