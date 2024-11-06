import tkinter as tk

class CourseMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="lightgreen")

        label = tk.Label(self, text="mode Cours", font=("Helvetica", 18), bg="lightgreen")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Retour", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("MainMenu")
