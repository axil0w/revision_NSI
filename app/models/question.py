import random
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

questions_qcm = [
    # Architecture
    ("Quels section n'appartient pas au diagramme de Van Neuman ?", ["Arithmetic unit", "Control unit", "Data unit", "Register"], "Data unit", ["diagramme", 0]),
    ("Qu'est ce que l'assembleur ?", ["La connexion entre les registres", "Le groupement des composants", "Un programme de base", "Le language de programmation initial"], "Le language de programmation initial", ["voc", 1]),
    ("Choisir le bon ordre du diagramme interface machine - utilisateur :", ["OS - Logiciel - matériel- utilisateur", "Matériel - OS - Logiciel - utilisateur", "OS - matériel - Logiciel - utilisateur", "Logiciel - utilisateur - OS - matériel"], "Matériel - OS - Logiciel - utilisateur", ["diagramme", 1]),
    ("Quelle est la différence entre #85 et 85 ?", ["85 est la valeur, #85 l'adresse 85", "#85 est la valeur, 85 l'adresse 85", "Il n'y en a pas : 85 et #85 sont la valeur", "Il n'y en a pas : 85 et #85 sont l'adresse"], "85 est la valeur, #85 l'adresse 85", ["voc", 2]),

    # Programmation orientée objet (OOP)
    ("Sélectionnez le Getter :", ["self.variable = var", "Setter", "return self.variable", "return Quechua"], "return self.variable", ["voc", 0]),
    ("Quels sont les différent types de variables spécifiques en Oop ?", ["Variables dynamiques", "Variables d'instances", "Variables de classes", "Objets"], ["Variables d'instances", "Variables de classes"], ["voc", 1]),
    ("Quels sont les avantages de la Oop ?", ["Encapsulation", "Lisibilité", "Ordination", "Instantiation"], ["Encapsulation", "Lisibilité"], ["oop", 0]),
    ("Syntaxe de la définition d'une classe :", ["class Exemple(object):", "class exemple:", "class Exemple:", "class Exemple()"], ["class Exemple(object):", "class Exemple:", "class Exemple()"], ["syntaxe", 1]),
    ("Quelles sont les possibilités de la Oop ?", ["Héritage", "Surcharge", "Arborescence", "Différence"], ["Héritage", "Surcharge"], ["oop", 1]),

    # Réseaux
    ("Comment s'appelle le service qui permet de faire le lien entre une IP et un nom de domaine ?", ["Internet", "DNS", "ARP", "HTTP"], "DNS", ["voc", 0]),
    ("Vous soupçonnez que des paquets se perdent entre votre ordinateur et leur destination. Quelle commande utiliseriez-vous pour trouver la source du problème efficacement ?", ["ipconfig", "traceroute", "nslookup", "ping"], "traceroute", ["code", 0]),
    ("Combien y-a-t-il de couches dans le modèle OSI ?", ["7", "5", "5", "6"], "7", ["schema", 1]),
    ("À quoi correspond le port 80 ?", ["HTTP", "SMTP", "FTP", "SSH"], "HTTP", ["voc", 1]),

    # Bases de Données (BDD)
    ("Quelle est la principale fonction d'un système de gestion de bases de données (SGBD) ?", ["Gérer le matériel informatique", "Stocker, modifier et extraire des données", "Créer des applications", "Assurer la sécurité des ordinateurs"], "Stocker, modifier et extraire des données", ["coo", 0]),
    ("Quel langage est utilisé pour interagir avec les bases de données relationnelles ?", ["HTML", "Java", "Python", "SQL"], "SQL", ["voc", 0]),
    ("Qu'est-ce qu'une clé primaire ?", ["Un identifiant unique pour chaque enregistrement", "Une colonne avec des valeurs nulles", "Un champ pour les relations entre tables", "Un mot-clé SQL"], "Un identifiant unique pour chaque enregistrement", ["voc", 1]),
    ("Quelle commande SQL récupère des données d'une table ?", ["INSERT", "UPDATE", "SELECT", "DELETE"], "SELECT", ["code", 0])
]

class Question(object):  # Pour les questions (type qcm par def)
    def __init__(self, question, proposition, answer, subject, category, eval):
        self.question = question  # queston en elle meme
        self.proposition = proposition  # differentes propositions
        self.answer = answer  # reponse
        self.subject = subject  # sujet plus precis de la question
        self.category = category  # theme de la question
        self.eval = eval  # si la question est une question d'evalution

        self.check_buttons = []  # Store references to check button frames
        # Store response variables for each option
        self.response_vars = []
        self.score = 0
        self.tries = 0

    def start(self, parent, nb_questions):
        self.questions_restantes = nb_questions
        self.create_canvas(parent)

    def create_canvas(self, parent):
        # Create main canvas
        self.canvas = tk.Canvas(parent, width=400, height=500, bg='#871E1C')
        self.canvas.pack(expand=True, fill='both', padx=0)

        # Create frame inside canvas for widgets
        frame = tk.Frame(self.canvas, bg="#871E1C")
        self.canvas.create_window(0, 0, window=frame, anchor='nw', )

        # Question label
        self.question_label = tk.Label(frame, text=self.question, wraplength=380, bg="#871E1C", fg="white")
        self.question_label.pack(pady=10, padx=10)

        # Load and store images as instance variables
        self.image_unchecked = ImageTk.PhotoImage(
            Image.open("app/assets/images/checkbox_off.png").resize((30, 30))
        )
        self.image_checked = ImageTk.PhotoImage(
            Image.open("app/assets/images/checkbox_on.png").resize((30, 30))
        )

        # Create check buttons for each proposition
        for i, prop in enumerate(self.proposition):
            # Create a BooleanVar for this option
            var = tk.BooleanVar()
            self.response_vars.append(var)

            # Create a frame for each option
            option_frame = tk.Frame(frame, bg="#871E1C")
            option_frame.pack(pady=2, padx=20, anchor='w')

            # Create label with image
            image_label = tk.Label(
                option_frame,
                bg="#871E1C",
                fg="white",
                image=self.image_unchecked,
                cursor='hand2'
            )
            image_label.pack(side='left', padx=(0, 10))

            self.bottom_frame = tk.Frame(self.canvas, bg="#871E1C")
            self.bottom_frame.pack(side='bottom', fill='x', pady=(20, 10))

            # Add spacer to push content to bottom
            tk.Frame(self.canvas, bg="#871E1C", height=50).pack(fill='x', expand=True)

            # Create text label
            text_label = tk.Label(
                option_frame,
                text=prop,
                bg="#871E1C",
                fg="white",
                cursor='hand2',
                font=("Montserra", 17)
            )
            text_label.pack(side='left')

            # Bind click events to both labels
            image_label.bind('<Button-1>', lambda e, v=var, idx=i: self.toggle_option(v, idx))
            text_label.bind('<Button-1>', lambda e, v=var, idx=i: self.toggle_option(v, idx))

            # Store reference to components
            self.check_buttons.append({
                'frame': option_frame,
                'image_label': image_label,
                'text_label': text_label,
                'value': prop,
                'var': var
            })

        # Validate button
        validate_button = tk.Button(
            self.bottom_frame,
            text="Valider",
            command=lambda: self.validate_answer(parent)
        )
        validate_button.pack(pady=10)

        # Subject and category labels
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='x', padx=10, pady=5)

        # Update scroll region after widgets are added
        frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.score+=1
        self.next_question(parent)
        return self.canvas

    def toggle_option(self, var, index):
        """Toggle the selected state of an option"""
        current_value = var.get()
        # Toggle current option
        var.set(not current_value)
        self.check_buttons[index]['image_label'].configure(
            image=self.image_checked if not current_value else self.image_unchecked
        )

    def validate_answer(self, parent):
        response = self.response_vars
        if response:
            is_correct = self.check_answer(response)
            self.tries += 1
            if not self.eval:
                for i, button in enumerate(self.check_buttons):
                    if button['text_label'].cget("text") in self.answer:
                        button['image_label'].configure(image=self.image_checked)
                        self.response_vars[i] = tk.BooleanVar(value=True)
                    else:
                        button['image_label'].configure(image=self.image_unchecked)
                        self.response_vars[i] = tk.BooleanVar(value=False)
            if is_correct:
                self.score += 1
                self.next_question(parent)

    def show_score(self, parent):
        # Create new window
        score_window = tk.Toplevel(parent)
        score_window.title("Score")
        score_window.geometry("400x200")
        score_window.configure(bg='#871E1C')

        # Center the window
        width = 400
        height = 200
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        score_window.geometry('%dx%d+%d+%d' % (width, height, x, y))

        # Add score label
        score_label = tk.Label(
            score_window,
            text=f"{self.score}/{self.tries}",
            bg='#871E1C',
            fg='white',
            font=("Helvetica", 60, "bold")
        )
        score_label.pack(expand=True)

        # Function to close window
        def close_window():
            score_window.destroy()

        # Schedule window closure
        score_window.after(5000, close_window)

    def next_question(self, parent):
        if self.questions_restantes == 0:
            self.show_score(parent)
            self.kill(parent)
        else:
            self.questions_restantes -= 1
            # Select new random question
            question = random.choice(questions_qcm)

            # Update question text
            self.question_label.configure(text=question[0])

            # Update instance variables
            self.question = question[0]
            self.proposition = question[1]
            self.answer = question[2]
            self.subject = question[3][0]
            self.category = question[3][1]

            # Clear existing check buttons
            for button in self.check_buttons:
                button['frame'].destroy()

            self.check_buttons = []
            self.response_vars = []

            # Create new check buttons for each proposition
            for i, prop in enumerate(self.proposition):
                # Create a BooleanVar for this option
                var = tk.BooleanVar()
                self.response_vars.append(var)

                # Create a frame for each option
                option_frame = tk.Frame(self.canvas, bg="#871E1C")
                option_frame.pack(pady=2, padx=20, anchor='w')

                # Create label with image
                image_label = tk.Label(
                    option_frame,
                    bg="#871E1C",
                    fg="white",
                    image=self.image_unchecked,
                    cursor='hand2'
                )
                image_label.pack(side='left', padx=(0, 10))

                # Create text label
                text_label = tk.Label(
                    option_frame,
                    text=prop,
                    bg="#871E1C",
                    fg="white",
                    cursor='hand2',
                    font=("Montserra", 17)
                )
                text_label.pack(side='left')

                # Bind click events to both labels
                image_label.bind('<Button-1>', lambda e, v=var, idx=i: self.toggle_option(v, idx))
                text_label.bind('<Button-1>', lambda e, v=var, idx=i: self.toggle_option(v, idx))

                # Store reference to components
                self.check_buttons.append({
                    'frame': option_frame,
                    'image_label': image_label,
                    'text_label': text_label,
                    'value': prop,
                    'var': var
                })


    def kill(self, parent):
        self.canvas.destroy()

    def get_question(self):
        return self.question

    def get_proposition(self):
        return self.proposition

    def get_theme(self):
        return self.category, self.subject

    def check_answer(self, prop):
        for i in range(len(prop)):  # verifie si rep au qcm juste
            if prop[i].get() != (self.proposition[i] in self.answer):
                return False
        return True



# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Question Example")

    # Example QCM
    qcm = Question(
        "Quelle est la capitale de la France?",
        ["Paris", "Londres", "Berlin", "Madrid"],
        "Paris",
        "Géographie",
        "Capitales"
    )

    # Create and pack the canvas
    question_canvas = qcm.create_canvas(root)

    root.mainloop()
