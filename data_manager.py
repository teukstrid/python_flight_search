import requests
import os

SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

class DataManager:

    def __init__(self):
        self.ticket_data = {}

    def get_ticket_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.ticket_data = data["prices"]
