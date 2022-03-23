import requests
import os
from datetime import date

# 100 Days of Python course
# Code written following the instructor
#   Except set_data_for_today() which she left as an example for the students to try on their own
#   Except update_data() which she left as an example for the students to try on their own
#   Except delete_data() which she left as an example for the students to try on their own

# ToDo: GUI interface to select date and enter # hours wrote that day


PIXELA_API_KEY = os.environ.get("PIXELA_API_KEY")
USERNAME = "judyth"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


# call once and only once per graph
def create_graph():
    user_params = {
        "token": PIXELA_API_KEY,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


# call once and only once per graph
def define_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_params = {
        "id": GRAPH_ID,
        "name": "Track Writing",
        "unit": "hour",
        "type": "float",
        "color": "sora",
        "timezone": "EST"
    }
    headers = {
        "X-USER-TOKEN": PIXELA_API_KEY,
    }
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)


def set_data_for_today():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    headers = {
        "X-USER-TOKEN": PIXELA_API_KEY,
    }
    parameters = {
        "date": date.today().strftime('%Y%m%d'),
        "quantity": "0.5",
    }
    response = requests.post(url=graph_endpoint, json=parameters, headers=headers)
    print(response.text)


# if data exists, overwrites it
def update_data():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}"
    headers = {
        "X-USER-TOKEN": PIXELA_API_KEY,
    }
    parameters = {
        "quantity": "1",
    }
    response = requests.put(url=graph_endpoint, json=parameters, headers=headers)
    print(response.text)


def delete_data():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}"
    headers = {
        "X-USER-TOKEN": PIXELA_API_KEY,
    }
    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)


# set_data_for_today()
# update_data()
delete_data()
