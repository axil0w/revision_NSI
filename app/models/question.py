import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

    def create_canvas(self, parent):
        # Create main canvas
        canvas = tk.Canvas(parent, width=400, height=500, bg='white')
        canvas.pack(expand=True, fill='both')

        # Create frame inside canvas for widgets
        frame = ttk.Frame(canvas)
        canvas.create_window(0, 0, window=frame, anchor='nw')

        # Question label
        question_text = self.question
        question_label = ttk.Label(frame, text=question_text, wraplength=380)
        question_label.pack(pady=10, padx=10)

        # Load and store images as instance variables
        self.image_unchecked = ImageTk.PhotoImage(
            Image.open("app\\assets\\images\\checkbox_off.png").resize((30, 30))
        )
        self.image_checked = ImageTk.PhotoImage(
            Image.open("app\\assets\\images\\checkbox_on.png").resize((30, 30))
        )

        # Create check buttons for each proposition
        for i, prop in enumerate(self.proposition):
            # Create a BooleanVar for this option
            var = tk.BooleanVar()
            self.response_vars.append(var)

            # Create a frame for each option
            option_frame = ttk.Frame(frame)
            option_frame.pack(pady=2, padx=20, anchor='w')

            # Create label with image
            image_label = ttk.Label(
                option_frame,
                image=self.image_unchecked,
                cursor='hand2'
            )
            image_label.pack(side='left', padx=(0, 10))

            # Create text label
            text_label = ttk.Label(
                option_frame,
                text=prop,
                cursor='hand2',
                font=("Montserra",17)
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
        validate_button = ttk.Button(
            frame,
            text="Valider",
            command=lambda: self.validate_answer(parent)
        )
        validate_button.pack(pady=10)

        # Subject and category labels
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='x', padx=10, pady=5)

        ttk.Label(info_frame, text=f"Sujet: {self.subject}").pack(side='left')
        ttk.Label(info_frame, text=f"Catégorie: {self.category}").pack(side='right')

        # Update scroll region after widgets are added
        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'))

        return canvas

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
            result_text = "Correct!" if is_correct else "Incorrect!"
            color = "green" if is_correct else "red"


            # Create result label
            result_label = ttk.Label(
                parent,
                text=result_text,
                foreground=color
            )
            result_label.pack(pady=5)
            if not self.eval:
                for i, button in enumerate(self.check_buttons):
                    if button['text_label'].cget("text") in self.answer:
                        button['image_label'].configure(image=self.image_checked)
                        self.response_vars[i] = tk.BooleanVar(value=True)
                    else:
                        button['image_label'].configure(image=self.image_unchecked)
                        self.response_vars[i] = tk.BooleanVar(value=False)


    

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

class TextQuestion(Question):  # Pour les question avec entrees
    def __init__(self, question, answer, proposition, subject, category):
        super().__init__(question, proposition, answer, subject, category)  # heritage de la classe questions

    def create_canvas(self, parent):
        canvas = tk.Canvas(parent, width=400, height=500, bg='white')
        canvas.pack(expand=True, fill='both')

        frame = ttk.Frame(canvas)
        canvas.create_window(0, 0, window=frame, anchor='nw')

        # Question label
        question_label = ttk.Label(frame, text=self.question, wraplength=380)
        question_label.pack(pady=10, padx=10)

        # Text entry
        self.response_var = tk.StringVar()
        entry = ttk.Entry(frame, textvariable=self.response_var)
        entry.pack(pady=10, padx=10)

        # Validate button
        validate_button = ttk.Button(
            frame,
            text="Valider",
            command=lambda: self.validate_answer(parent)
        )
        validate_button.pack(pady=10)

        # Subject and category info
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='x', padx=10, pady=5)

        ttk.Label(info_frame, text=f"Sujet: {self.subject}").pack(side='left')
        ttk.Label(info_frame, text=f"Catégorie: {self.category}").pack(side='right')

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'))

        return canvas

    def check_enter(self, prop):  # verifie si entree juste
        proposition = prop.isalnum().lower()  # format evitant des erreurs de mise en forme (exe : maj)
        answer = self.answer.isalnum().lower()
        return proposition == answer

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