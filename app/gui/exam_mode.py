import tkinter as tk


class ExamMode(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.configure(bg="#0B6E4F")

        label = tk.Label(self, text="Mode examen", font=("Helvetica", 18), bg="#0B6E4F")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Retour", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        self.switch_frame("MainMenu")
