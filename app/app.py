import tkinter as tk
from app.gui.mainmenu import MainMenu
from app.gui import *
from app.gui.revision_mode import RevisionMode
from app.gui.exam_mode import ExamMode
from app.gui.course_mode import CourseMode
from app.gui.usermenu import UserMenu
class NSIQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NSI Quiz Platform")
        self.geometry("800x600")
        self.frames = {}
        self.bind("<Escape>", self.quitting)
        self.bind("<F11>", self.fullscreen)

        self.attributes("-fullscreen", True)

        # Création de toutes les frames
        for frame_class in (MainMenu, RevisionMode, CourseMode, ExamMode, UserMenu,ArchitecturePage,ReseauxPage,OopPage,BddPage):
            frame = frame_class(self, self.show_frame)
            self.frames[frame_class.__name__] = frame

        self.show_frame("MainMenu")


    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(expand=True, fill="both")

    def fullscreen(self, event=None):
        self.state = not self.state
        self.attributes("-fullscreen", self.state)

    def quitting(self, event):
        print("fin")
        self.quit()
