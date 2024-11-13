import tkinter as tk
from PIL import Image, ImageTk

class CourseMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame #switch de frame
        self.bg_color = "#2B4162"#couleur du bg
        self.button_color = "#FA9F42"#couleur du Bouton 
        self.text_color = "#F0BCC5"#couleur du texte
        self.highlight_color = "#0B6E4F"#couleur de la surbrillance
        self.configure(bg=self.bg_color)#configuration de la page avec la couleure du bg

        self.create_widgets()#utilisation de la fonction create_widgets()
        self.show_view()#utilisation de la fonction show_views()

    def create_widgets(self):
        """
        Crée les widgets de la page
        """
        self.label = tk.Label(
            self, text="Mode Cours", font=("Montserrat", 24, "bold"), 
            fg=self.text_color, bg=self.bg_color
        )#création d'un label mode cours (texte)

        self.back_button = tk.Button(
            self, text="Retour", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )#création d'un bouton retour avec comme commande la fonction goback activefg et activebg servent a mettre un bouton dynamique

        self.button1 = tk.Button(
            self, text="Architecture", command=self.go_to_ArchitecturePage, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )#création du premier bouton

        self.button2 = tk.Button(
            self, text="Bases De données", command=self.go_to_ReseauxPage, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )#création du deuxieme bouton

        self.button3 = tk.Button(
            self, text="Programmation orienté objet", command=self.go_to_OopPage, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )#création du troisieme bouton

        self.button4 = tk.Button(
            self, text="Réseaux", command=self.go_to_BddPage, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )#création du quatrieme bouton

    def show_view(self):
        """
        pack tout les boutons et tout les labels sur la page
        """
        self.label.pack(pady=20)
        self.back_button.pack(pady=10)

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)
        self.button4.pack(pady=10)

    def go_back(self):
        """
        revient a la Frame MainMenu
        """
        self.switch_frame("MainMenu")

    def go_to_ArchitecturePage(self):
        """
        Revient a la frame ArchitecturePage
        """
        self.switch_frame("ArchitecturePage")

    def go_to_ReseauxPage(self):
        self.switch_frame("BddPage")

    def go_to_OopPage(self):
        """
        Revient a la frame ArchitecturePage
        """
        self.switch_frame("OopPage")

    def go_to_BddPage(self):
        """
        Revient a la frame reseaux
        """
        self.switch_frame("ReseauxPage")


class ArchitecturePage(tk.Frame):#classe architecture avec creation de frame
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.bg_color = "#2B4162"  
        self.button_color = "#FA9F42"
        self.text_color = "#F0BCC5"
        self.highlight_color = "#0B6E4F"
        self.configure(bg=self.bg_color)
        self.create_widgets() 

    def create_widgets(self):
        self.image_archicours1 = Image.open("app/assets/images/archicours2.png")
        self.image_archicours1 = self.image_archicours1.resize((500, 700))  
        self.photo1 = ImageTk.PhotoImage(self.image_archicours1)
        """
        Creation des widgets de la page architecture
        """
        self.image_archicours1 = Image.open("app/assets/images/archicours2.png")#ouvre l'image archi cours
        self.image_archicours1 = self.image_archicours1.resize((500, 700)) #resize l'image
        self.photo1 = ImageTk.PhotoImage(self.image_archicours1)#transforme l'image en image lisible par tkinter

        self.image_archicours2 = Image.open("app/assets/images/architecturefiche.png")
        self.image_archicours2 = self.image_archicours2.resize((500, 700))  
        self.photo2 = ImageTk.PhotoImage(self.image_archicours2)

        self.image_archicours3 = Image.open("app/assets/images/interfacefiche.png")
        self.image_archicours3 = self.image_archicours3.resize((500, 700))  
        self.photo3 = ImageTk.PhotoImage(self.image_archicours3)

        self.label = tk.Label(self, text="ArchitecturePage", font=("Montserrat", 24, "bold"), fg=self.text_color, bg=self.bg_color)

        self.image_label1 = tk.Label(self, image=self.photo1, bg=self.bg_color)  
        self.image_label2 = tk.Label(self, image=self.photo2, bg=self.bg_color)  
        self.image_label3 = tk.Label(self, image=self.photo3, bg=self.bg_color)  

        self.back_button = tk.Button(
            self, text="Go Back", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

        self.label.pack(pady=20)
        
        self.image_label1.pack(side=tk.LEFT, padx=10)#position des images sur la gauche avec un paddinx sur l'axe x de 10 chaqun
        self.image_label2.pack(side=tk.LEFT, padx=10)  
        self.image_label3.pack(side=tk.LEFT, padx=10)  
        
        self.back_button.pack(pady=10)#affichage sur la page

    def go_back(self):
        self.switch_frame("CourseMode")
        """
        revient a la Frame CoursMode
        """
        self.switch_frame("CourseMode")

class ReseauxPage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame#meme chose 
        self.bg_color = "#2B4162"
        self.button_color = "#FA9F42"
        self.text_color = "#F0BCC5"
        self.highlight_color = "#0B6E4F"
        self.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        # Image
        self.image = Image.open("app/assets/images/reseauxcours.png")
        """
        Création des widgets de la page reseaux
        """
        self.image = Image.open("app/assets/images/reseauxcours.png")
        self.image = self.image.resize((600, 800))  
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, text="ReseauxPage", font=("Montserrat", 24, "bold"), fg=self.text_color, bg=self.bg_color)
        self.image_label = tk.Label(self, image=self.photo, bg=self.bg_color)  

        self.back_button = tk.Button(
            self, text="Go Back", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

        self.label.pack(pady=20)
        self.image_label.pack(pady=20) 
        self.back_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("CourseMode")
        """
        Revient a la frame CoursMode
        """
        self.switch_frame("CourseMode")


class OopPage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.bg_color = "#2B4162"
        self.button_color = "#FA9F42"
        self.text_color = "#F0BCC5"
        self.highlight_color = "#0B6E4F"
        self.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        # Image
        self.image = Image.open("app/assets/images/oopcours.png")
        """
        Creation des widgets de la page sur la programmation orienté objet
        """
        self.image = Image.open("app/assets/images/oopcours.png")
        self.image = self.image.resize((600, 800)) 
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, text="OopPage", font=("Montserrat", 24, "bold"), fg=self.text_color, bg=self.bg_color)
        self.image_label = tk.Label(self, image=self.photo, bg=self.bg_color) 

        self.back_button = tk.Button(
            self, text="Go Back", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

        self.label.pack(pady=20)
        self.image_label.pack(pady=20) 
        self.back_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("CourseMode")
        """
        Revient a la frame Cours mode 
        """
        self.switch_frame("CourseMode")


class BddPage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.bg_color = "#2B4162"
        self.button_color = "#FA9F42"
        self.text_color = "#F0BCC5"
        self.highlight_color = "#0B6E4F"
        self.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        """
        crée les widgets pour la page sur les bases de données
        """
        # Image
        self.image = Image.open("app/assets/images/bddfiche.png")
        self.image = self.image.resize((600, 800))  
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, text="BddPage", font=("Montserrat", 24, "bold"), fg=self.text_color, bg=self.bg_color)
        self.image_label = tk.Label(self, image=self.photo, bg=self.bg_color)  

        self.back_button = tk.Button(
            self, text="Go Back", command=self.go_back, font=("Montserrat", 14, "bold"),
            fg=self.text_color, bg=self.button_color, borderwidth=0,
            activebackground=self.highlight_color, activeforeground=self.text_color
        )

        self.image_label.pack(pady=20)  
        self.back_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("CourseMode")
        """
        Revient sur la page CoursMode
        """
        self.switch_frame("CourseMode")
