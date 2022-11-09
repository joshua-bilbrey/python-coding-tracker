import requests
import os

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "python"
print(USERNAME, TOKEN)

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_user():
    # create user (successful) -- https://pixe.la/
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_new_graph():
    # create a graph
    graph_params = {
        "id": GRAPH_ID,
        "name": "Python Daily Learning",
        "unit": "min",
        "type": "float",
        "color": "ajisai",
    }

    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)


def post_pixel(date, quantity):
    # post a pixel of data
    pixel_data_params = {
        "date": date,
        "quantity": f"{quantity}",
    }

    response = requests.post(url=pixel_data_endpoint, json=pixel_data_params, headers=headers)
    print(response.text)


def update_name(name):
    # post a pixel of data
    name_params = {
        "name": name,
    }

    response = requests.put(url=pixel_data_endpoint, json=name_params, headers=headers)
    print(response.text)


def update_pixel(date, quantity):
    # update a pixel for a specific date
    update_pixel_data_params = {
        "quantity": f"{quantity}",
    }

    response = requests.put(url=f"{pixel_data_endpoint}/{date}", json=update_pixel_data_params, headers=headers)
    print(f"{pixel_data_endpoint}/{date}")
    print(response.text)


def delete_pixel(date):
    # delete a pixel
    response = requests.delete(url=f"{pixel_data_endpoint}/{date}", headers=headers)
    print(response.text)
