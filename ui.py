#MIT License Copyright (c) 2023 Saiyam Jain

import customtkinter as ctk
import tkinter as tk
from PIL import Image
from quiz_brain import QuizBrain, new_quiz

THEME_COLOR = "#375362"

class Ui():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.win = tk.Tk()
        self.win.title("Quizzler")
        self.win.iconbitmap("images\\icon.ico")
        self.win.resizable(False, False)
        self.win.config(background = THEME_COLOR, padx = 10, pady = 10)

        self.score_text = ctk.CTkLabel(self.win, text= f"Score: {self.quiz.score}", font = ("Arial", 20), text_color = "white", fg_color = THEME_COLOR)
        self.score_text.grid(column = 1, sticky = "e", pady = (0, 20))

        self.canvas = tk.Canvas(self.win, height = 400, width = 400, background = "white")
        self.canvas.grid(column = 0, row = 1, columnspan = 2)

        self.question_text = self.canvas.create_text(200, 200, text = "Questions here", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 400)
        self.get_next_question()

        restart_img = ctk.CTkImage(light_image = Image.open("images\\restart.png"), dark_image = Image.open("images\\restart.png"), size = (75, 75))
        self.restart_button = ctk.CTkButton(self.win, image = restart_img, text = "", height = 97, width = 100, command = self.restart_game)
        self.restart_button.grid(column = 1, row = 2, pady = (20,0), columnspan = 2)
        self.restart_button.grid_forget()

        true_img = ctk.CTkImage(light_image = Image.open("images\\true.png"), dark_image = Image.open("images\\true.png"), size = (75, 75))
        self.true_button = ctk.CTkButton(self.win, image = true_img, text = "", height = 97, width = 100, command = lambda : self.get_next_question("True"))
        self.true_button.grid(column = 0, row = 2, pady = (20, 0))

        false_img = ctk.CTkImage(light_image = Image.open("images\\false.png"), dark_image = Image.open("images\\false.png"), size = (75, 75))
        self.false_button = ctk.CTkButton(self.win, image = false_img, text = "", height = 100, width = 100, command = lambda : self.get_next_question("False"))
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
            self.score_text.configure(text = f"Score: {self.quiz.score}")

    def restart_game(self):
        self.score_text.configure(text= "Score: 0")
        self.score_text.grid(column = 1, row = 0, sticky = "e", pady = (0, 20))
        self.quiz = new_quiz()
        self.get_next_question()
        self.restart_button.grid_forget()
        self.true_button.grid(column = 0, row = 2, pady = (20, 0))
        self.false_button.grid(column = 1, row = 2, pady = (20, 0))
        self.canvas.delete(self.score_display)






