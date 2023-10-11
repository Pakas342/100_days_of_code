import requests
from datetime import datetime
import os

NUTRITION_ID = os.environ["NUTRITION_ID"]
NUTRITION_API_KEY = os.environ["NUTRITION_API_KEY"]
EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

NOW = datetime.now()
str_date = NOW.strftime("%Y/%m/%d")
str_hour = NOW.strftime("%H:%M:%S")
# print(str_date)

exercise_header = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json"
}

user_prompt = input("Write the exercise you did: ")

exercise_body = {
    "query": user_prompt,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 24
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_body, headers=exercise_header)
exercise_response.raise_for_status()
# print(exercise_response.json())

activities = [activity for activity in exercise_response.json()["exercises"]]

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for activity in activities:
    sheety_body = {
        "workout": {
            "date": str_date,
            "time": str_hour,
            "exercise": activity["name"].title(),
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_header)
    sheety_response.raise_for_status()
    print(sheety_response.status_code)
    print(sheety_response.json())