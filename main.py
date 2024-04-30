from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_Manager = DataManager()
flight_Search = FlightSearch()
notification_Manager = NotificationManager()

data_Manager.get_ticket_data()

for destination in data_Manager.ticket_data:
    found_flight = flight_Search.find_flights(destination)
    if found_flight:
        notification_Manager.send_message(
            message=f"You found a great price. You can travel to {found_flight.arrival_dest} from {found_flight.departure_dest} for only"
                    f"{found_flight.price}kr for {found_flight.nights_in_dest} nights. Go here to book:"
                    f"{found_flight.booking_link}"
        )
    else:
        print("nothing found")
