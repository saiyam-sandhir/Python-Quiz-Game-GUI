#MIT License Copyright (c) 2023 Saiyam Jain

import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        #This funtion checks if there are question left in the list of question objects
        return self.question_number < len(self.question_list)

    def next_question(self):
        #This function returns the text of a question from the next question object in the list
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
