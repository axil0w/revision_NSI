import tkinter as tk

class UserMenu(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="lightgreen")
        
        label = tk.Label(self, text="Voici la liste des Utilisateurs!", font=("Montserrat", 18), bg="lightgreen")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Retour", command=self.go_back)
        back_button.pack(pady=10)
        
        adduser_button= tk.Button(self,text="ajout user", command=self.add_user)
        adduser_button.pack(pady=10)
    def go_back(self):
        """
        Fonction qui revient au menu princ
        """
        self.switch_frame("MainMenu")
    def add_user(self):
        	pass
