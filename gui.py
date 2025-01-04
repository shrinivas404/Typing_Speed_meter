import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Typing Speed Meter")
        self.window.config(bg='black')
        self.window.minsize(600, 600)

        self.highest_score()
        self.window.mainloop()

    def highest_score(self):
        highest_score_label = tk.Label(text="Highest score is {score here}", font=("Ariel", 25), fg='blue', bg='black')
        highest_score_label.grid(row=3, column=0, padx=20, pady=20)

