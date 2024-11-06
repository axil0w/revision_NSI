import tkinter as tk
from PIL import Image, ImageTk

# Classe pour le menu principal
class MainMenu(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master, bg="#2B4162")  
        self.switch_frame = switch_frame

        # Crée les widgets
        self.create_widgets()

    def create_widgets(self):
        """Crée et place tous les widgets de l'interface utilisateur"""
        
        # Titre du quizz de NSI centré
        self.title_label = tk.Label(self, text="QUIZZ NSI", font=("Montserrat", 50), fg="white", bg="#2B4162")
        self.title_label.pack(pady=50)  

        # Créer un frame pour empiler les boutons en ligne (les uns au-dessus des autres)
        button_frame = tk.Frame(self, bg="#2B4162")  
        button_frame.pack(pady=50)

        # Charger les images pour les icônes des boutons
        self.icon_revision = ImageTk.PhotoImage(Image.open("revisions.png").resize((30, 30)))
        self.icon_cours = ImageTk.PhotoImage(Image.open("cours.png").resize((30, 30)))
        self.icon_exam = ImageTk.PhotoImage(Image.open("exam.png").resize((30, 30)))

        # Bouton Révision avec icône
        self.revision_button = tk.Button(button_frame, text="  Mode Révision ", font=("Montserrat", 16),
                                         image=self.icon_revision, compound="left", 
                                         command=self.open_revision_mode, padx=20, pady=10,
                                         bg="#1F6F8B", fg="white", relief="flat")
        self.revision_button.pack(fill="x", pady=10)

        # Bouton Cours avec icône
        self.cours_button = tk.Button(button_frame, text="   Mode Cours    ", font=("Montserrat", 16),
                                    image=self.icon_cours, compound="left",  
                                      command=self.open_cours_mode, padx=20, pady=10,
                                      bg="#1F6F8B", fg="white", relief="flat")
        self.cours_button.pack(fill="x", pady=10)

        # Bouton Examen avec icône
        self.exam_button = tk.Button(button_frame, text=" Mode Examen  ", font=("Montserrat", 16),
                                     image=self.icon_exam, compound="left",  
                                     command=self.open_exam_mode, padx=20, pady=10,
                                     bg="#1F6F8B", fg="white", relief="raised")
        self.exam_button.pack(fill="x", pady=10)

        # Bouton "users" en haut à gauche avec image détourée
        self.user_image = Image.open("login.png").resize((150, 150))
        self.user_image = ImageTk.PhotoImage(self.user_image)

        # Utilisation d'un Canvas pour afficher l'image du bouton utilisateur
        self.user_canvas = tk.Canvas(self, width=150, height=150, highlightthickness=0, bg="#2B4162")  
        self.user_canvas.place(x=10, y=10)
        self.user_canvas.create_image(75, 75, image=self.user_image)  # Centré dans le Canvas
        self.user_canvas.bind("<Button-1>", lambda event: self.open_user_menu())  

    def open_revision_mode(self):
        """Fonction pour passer en mode révision"""
        self.switch_frame("RevisionMode")

    def open_cours_mode(self):
        """Fonction pour passer en mode cours"""
        self.switch_frame("CoursMode")

    def open_exam_mode(self):
        """Fonction pour passer en mode examen"""
        self.switch_frame("ExamMode")

    def open_user_menu(self):
        """Fonction pour ouvrir le menu utilisateur"""
        self.switch_frame("UserMenu")
