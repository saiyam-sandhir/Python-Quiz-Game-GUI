#MIT License Copyright (c) 2023 Saiyam Jain

#This module retrieves question data using Open Trivial Database API
import requests

NUMBER_OF_QUESTIONS = 10

def get_data(num_of_questions = NUMBER_OF_QUESTIONS):

    response = requests.get(url = f"https://opentdb.com/api.php?amount={num_of_questions}&type=boolean")
    response.raise_for_status()

    question_data = response.json()["results"]

    return question_data
