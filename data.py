import requests

DATA_URL = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean",
}

quiz_response = requests.get(url=DATA_URL, params=params)
quiz_response.raise_for_status()

question_data = quiz_response.json()["results"]
