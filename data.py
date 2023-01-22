#This module retrieves question data using Open Trivial Database API

import requests

NUMBER_OF_QUESTIONS = 10

response = requests.get(url = f"https://opentdb.com/api.php?amount={NUMBER_OF_QUESTIONS}&type=boolean")
response.raise_for_status()

question_data = response.json()["results"]