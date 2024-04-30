import requests
from datetime import datetime, timedelta
from flight_data import FlightData
import os

flight_endpoint = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_KEY = os.environ["FLIGHT_KEY"]

today_date = datetime.now().strftime("%Y-%m-%d")
dt = datetime.now()
td = timedelta(days=200)
date_to = dt + td
formatted_date_to = date_to.strftime("%Y-%m-%d")


class FlightSearch:

    def find_flights(self, destination):
        headers = {'apikey': FLIGHT_KEY}
        query = {
            'fly_from': "CPH",
            'fly_to': destination["iataCode"],
            'date_from': today_date,
            'date_to': formatted_date_to,
            'return_from': today_date,
            'return_to': formatted_date_to,
            'nights_in_dst_from': destination["nightsFrom"],
            'nights_in_dst_to': destination["nightsTo"],
            'price_from': 0,
            'price_to': destination["lowestPrice"],
            'adults': destination["adults"],
            'children': destination["children"],
            'flight_type': "round",
            'max_stopovers': 0,
            'one_for_city': 1,
            'curr': "SEK"
        }

        response = requests.get(url=flight_endpoint, params=query, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("No flights found for your selected destinations")
            return None

        flight_data = FlightData(
            departure_dest = data["cityFrom"],
            arrival_dest = data["cityTo"],
            departure_date = data["local_departure"],
            nights_in_dest = data["nightsInDest"],
            price = data["price"],
            booking_link = data["deep_link"],
        )
        print(f"Travel from {flight_data.departure_dest} for the low price of {flight_data.price}")
        return flight_data
