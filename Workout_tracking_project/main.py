import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('API_FOR_WORKOUT_TRAKING_PROJECT.env')
load_dotenv(dotenv_path=dotenv_path)

GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 160
AGE = 20

APP_ID = os.getenv("NT_APP_ID")
API_KEY = os.getenv("NT_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6190bc00bf575d910408b26a101c5c87/workout/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
print(result['exercises'][0]['nf_calories'])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.getenv("USERNAME"),
            os.getenv("PASSWORD"),
        )
    )

    #Bearer Token
    # bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)
