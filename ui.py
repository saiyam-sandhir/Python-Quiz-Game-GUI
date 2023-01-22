import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Ui():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.win = tk.Tk()
        self.win.title("Quizzler")
        self.win.config(padx = 20, pady = 20, background = THEME_COLOR)

        self.score_text = tk.Label(text = f"Score: {self.quiz.score}", font = ("Arial", 10), foreground = "white", background = THEME_COLOR)
        self.score_text.grid(column = 1, sticky = "e", pady = (0, 20))

        self.canvas = tk.Canvas(height = 400, width = 400, background = "white")
        self.canvas.grid(column = 0, row = 1, columnspan = 2)

        self.question_text = self.canvas.create_text(200, 200, text = "Questions here", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 400)
        self.get_next_question()

        ture_img = tk.PhotoImage(file = "images\\true.png")
        self.ture_button = tk.Button(image = ture_img, height = 97, width = 100, highlightthickness = 0, relief = "flat", command = lambda : self.get_next_question("True"))
        self.ture_button.grid(column = 0, row = 2, pady = (20, 0))

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
            self.canvas.itemconfig(self.question_text, text = "You have complete the quiz")
            self.canvas.create_text(200, 240, text = f"YOUR SCORE: {self.quiz.score}", font = ("Arial", 20, "bold"), fill = "red", width = 400)
            self.score_text.destroy()

    def check_answer(self, ans):
        correct_answer = self.quiz.current_question.answer
        if ans == correct_answer:
            self.quiz.score += 1
            self.score_text.config(text = f"Score: {self.quiz.score}")



