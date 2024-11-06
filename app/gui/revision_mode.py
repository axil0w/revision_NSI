import tkinter as tk

class RevisionMode(tk.Frame):#tk.frame crée une section dans la fenetre
    def __init__(self, master, switch_frame):
        super().__init__(master)#classe hérité avec super et Master devient le parent
        self.switch_frame = switch_frame#changement de fenetre
        self.configure(bg="lightblue")#arriere plan

        label = tk.Label(self, text="le mode Révision", font=("Helvetica", 18), bg="lightblue")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Retour", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        """
        Fonction qui revient au menu princ
        """
        self.switch_frame("MainMenu")
