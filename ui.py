#MIT License Copyright (c) 2023 Saiyam Jain

import tkinter as tk
from quiz_brain import QuizBrain, new_quiz

THEME_COLOR = "#375362"

class Ui():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.win = tk.Tk()
        self.win.title("Quizzler")
        self.win.config(padx = 20, pady = 20, background = THEME_COLOR)

        self.score_text = tk.Label(text= f"Score: {self.quiz.score}", font = ("Arial", 10), foreground = "white", background = THEME_COLOR)
        self.score_text.grid(column = 1, sticky = "e", pady = (0, 20))

        self.canvas = tk.Canvas(height = 400, width = 400, background = "white")
        self.canvas.grid(column = 0, row = 1, columnspan = 2)

        self.question_text = self.canvas.create_text(200, 200, text = "Questions here", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 400)
        self.get_next_question()

        restart_img = tk.PhotoImage(file = "images\\restart.png")
        self.restart_button = tk.Button(image = restart_img, height = 97, width = 100, highlightthickness = 0, relief = "flat", command = self.restart_game)
        self.restart_button.grid(column = 1, row = 2, pady = (20,0), columnspan = 2)
        self.restart_button.grid_forget()

        true_img = tk.PhotoImage(file = "images\\true.png")
        self.true_button = tk.Button(image = true_img, height = 97, width = 100, highlightthickness = 0, relief = "flat", command = lambda : self.get_next_question("True"))
        self.true_button.grid(column = 0, row = 2, pady = (20, 0))

        false_img = tk.PhotoImage(file = "images\\false.png")
        self.false_button = tk.Button(image = false_img, height = 97, width = 100, highlightthickness = 0, relief = "flat", command = lambda : self.get_next_question("False"))
        self.false_button.grid(column = 1, row = 2, pady = (20, 0))

        self.win.mainloop()

    def get_next_question(self, ans = None):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text) 
            self.check_answer(ans)

        else:
            self.score_text.grid_forget()
            self.canvas.itemconfig(self.question_text, text = "You have complete the quiz")
            self.score_display = self.canvas.create_text(200, 240, text = f"YOUR SCORE: {self.quiz.score}", font = ("Arial", 20, "bold"), fill = "red", width = 400)
            self.true_button.grid_forget()
            self.false_button.grid_forget()
            self.restart_button.grid(column = 0, row = 2, pady = (20,0), columnspan = 2)

    def check_answer(self, ans):
        correct_answer = self.quiz.current_question.answer
        if ans == correct_answer:
            self.quiz.score += 1
            self.score_text.config(text = f"Score: {self.quiz.score}")

    def restart_game(self):
        self.score_text.config(text= "Score: 0")
        self.score_text.grid(column = 1, row = 0, sticky = "e", pady = (0, 20))
        self.quiz = new_quiz()
        self.get_next_question()
        self.restart_button.grid_forget()
        self.true_button.grid(column = 0, row = 2, pady = (20, 0))
        self.false_button.grid(column = 1, row = 2, pady = (20, 0))
        self.canvas.delete(self.score_display)






