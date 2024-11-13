import tkinter as tk
from PIL import Image, ImageTk

from app.models.question import Question


class RevisionMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        self.bg_color = "#2B4162"
        self.button_color = "#FA9F42"
        self.title_color = "#871E1C"
        self.highlight_color = "#0B6E4F"
        self.text_color = "#F0BCC5"

        self.create_widgets()

        self.show_initial_view()

    def create_widgets(self):
        """Crée et configure les widgets de l'interface RevisionMode"""

        self.configure(bg=self.bg_color)

        self.title_label = tk.Label(
            self, text="Mode Révision", font=("Montserrat", 24, "bold"),
            fg=self.title_color, bg=self.bg_color
        )

        self.revision_image = Image.open("app/assets/images/enter.png")
        self.revision_image = self.revision_image.resize((80, 80))
        self.revision_image = ImageTk.PhotoImage(self.revision_image)

        self.enter_button = tk.Button(
            self, image=self.revision_image, command=self.show_revision_view,
            borderwidth=0, bg=self.button_color, activebackground=self.highlight_color
        )

        self.back_button = tk.Button(
            self, text="Retour", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

        self.new_content_label = tk.Label(
            self, text="Bienvenue dans la révision !", font=("Montserrat", 20),
            fg=self.bg_color, bg=self.highlight_color
        )

        self.back_to_main_button = tk.Button(
            self, text="Retour au menu principal", command=self.go_back,
            font=("Montserrat", 14, "bold"), fg=self.text_color,
            bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

    def show_initial_view(self):
        """Affiche la vue initiale du mode révision."""
        self.configure(bg=self.bg_color)

        self.title_label.pack(pady=20)
        self.enter_button.pack(pady=10)
        self.back_button.pack(pady=10)


    def show_revision_view(self):
        self.title_label.pack_forget()
        self.enter_button.pack_forget()
        self.back_button.pack_forget()

        self.configure(bg=self.highlight_color)
        self.new_content_label.pack(pady=20)
        self.back_to_main_button.pack(pady=10)

        self.question = Question("rrr", ("ah", "r"), ("ah"), "OOP", "e", False)
        self.question.start(self, 10)

    def go_back(self):
        """Retourne au menu principal ou à la vue initiale du mode révision."""
        # Masque les widgets de la vue de révision
        self.new_content_label.pack_forget()
        self.back_to_main_button.pack_forget()

        # Réaffiche l'interface initiale
        self.show_initial_view()
        self.question.kill(self)
        # Retourne au menu principal
        self.switch_frame("MainMenu")
