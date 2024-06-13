import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('Habit traking.env')
load_dotenv(dotenv_path=dotenv_path)

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv('PIXE_TOKEN')
USERNAME = os.getenv('PIXE_USERNAME')
GRAPH_ID = os.getenv('PIXE_GRAPH_ID')

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixcel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
user_input = input("which habit do you want to track? ")
pixcel_data = {
    "date": today.strftime("%Y%m%d"),  # strftime is a method to display the time in the formated method. the string i
    # provide that will give the full year, month and day.
    "quantity": input(f"How many hour did you {user_input}? "),
}

response = requests.post(url=pixcel_creation_endpoint, json=pixcel_data, headers=headers)
print(response.text)


# UPDATE REQUEST: -
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# new_pixel_data = {
#     "quantity": "3.5"
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# DELETE REQUEST :-
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
