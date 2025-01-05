import tkinter as tk
import random
from tkinter import END

from passage_creator import clean_passage_list
import time


class GUI:
    def __init__(self):
        self.user_passage = []
        self.count = 0
        self.window = tk.Tk()
        self.window.title("Typing Speed Meter")
        self.window.minsize(800, 600)
        self.passage = random.choice(clean_passage_list)
        self.create_passage_box()
        self.canvas_fun(60)
        self.submit_button()
        # self.highest_score()
        self.typing_box()
        self.window.mainloop()

    # def highest_score(self):
    #     highest_score_label = tk.Label(self.window, text="Highest score is {score here}", font=("Ariel", 25), fg='blue',)
    #     highest_score_label.grid(row=3, column=0, padx=20, pady=20)

    def create_passage_box(self):
        passage_box = tk.Label(self.window,justify='left',wraplength=800, text=self.passage, font=("Ariel", 30))
        passage_box.grid(row=0, column=0, padx=20, pady=20)

    def typing_box(self):
        self.typing_box_text = tk.Text(self.window, height = 5,
                          wrap = tk.WORD, padx = 10, pady = 10)
        self.typing_box_text.grid(row=1, column=0, pady=20)


    def submit_button(self):
        submit = tk.Button(text="Submit",bg='green', command=self.calculate_speed, width=25, font=("Ariel", 15, "bold"))
        submit.grid(row=2, column=0, pady=30)

    def calculate_speed(self):
        timer = self.count
        user_passage = list(self.typing_box_text.get("1.0", END))
        speed = len(user_passage) - 1 /  timer * 60
        accuracy = self.calculate_accuracy()
        print(f"Speed is {speed} char/min\n{accuracy}")
        time.sleep(3)
        self.window.quit()

    def calculate_accuracy(self):
        passage =list(self.passage)
        user_passage = list(self.typing_box_text.get("1.0",END))
        correct_typing = 0
        for index in range (0, len(user_passage) - 1):
            if passage[index] == user_passage[index]:
                correct_typing += 1

        total_accuracy = f"Accuracy - {correct_typing / (len(user_passage)- 1) * 100} %"
        return total_accuracy

    def canvas_fun(self, count):
        canvas = tk.Canvas(width=200, height=223, highlightthickness=0)
        timer_text = canvas.create_text(100, 125, text="60", font=("Ariel", 35, "bold"))
        canvas.grid(row=0, column=1, padx=20, pady=20)

        canvas.itemconfig(timer_text, text=count)
        self.count = count
        if count == 0:
            self.calculate_speed()
        self.window.after(1000, self.canvas_fun, count - 1)