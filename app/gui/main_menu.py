from app.gui import exam_mode, revision_mode, course_mode
import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, master, switch_frame="MainMenu"):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="white")

        # Titre du quizz de NSI
        self.title_label = tk.Label(self, text="Quizz NSI", font=("Helvetica", 24), bg="white")
        self.title_label.pack(pady=20)

        # Boutons du menu
        self.revision_button = tk.Button(self, text="Mode Révision", command=self.open_revision_mode)
        self.revision_button.pack(pady=10)

        self.cours_button = tk.Button(self, text="Mode Cours", command=self.open_cours_mode)
        self.cours_button.pack(pady=10)

        self.exam_button = tk.Button(self, text="Mode Examen", command=self.open_exam_mode)
        self.exam_button.pack(pady=10)

    def open_revision_mode(self):
        """
        Fonction pour passer en mode revision
        """
        self.switch_frame("RevisionMode")

    def open_cours_mode(self):
        """
        Fonction pour passer en mode cours
        """
        self.switch_frame("CourseMode")

    def open_exam_mode(self):
        """
        Fonction pour passer en mode examen
        """
        self.switch_frame("ExamMode")



