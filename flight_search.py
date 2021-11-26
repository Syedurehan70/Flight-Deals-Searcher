import requests
import os
from flight_data import FlightData

KIWI_API_KEY = os.environ.get("kiwi_api_key")
kiwi_endpoint = "https://tequila-api.kiwi.com"

header = {
    "apikey": KIWI_API_KEY,
}


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, name):

        # getting city's iata code, returning it to main.py
        location_endpoint = f"{kiwi_endpoint}/locations/query"
        loc_params = {
            "term": name,
            "location_types": "city",
        }
        code_response = requests.get(url=location_endpoint, params=loc_params, headers=header)
        location_code = code_response.json()['locations'][0]['code']
        return location_code

    def search_with_zero_stops(self, dest, tom, to):

        # searching for available flights b/w defined period
        self.search_endpoint = f"{kiwi_endpoint}/v2/search"
        self.search_para = {
            "fly_from": "LON",
            "fly_to": dest,
            "date_from": tom,
            "date_to": to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "via_city": "",
            "curr": "GBP",
        }
        search_response = requests.get(url=self.search_endpoint, params=self.search_para, headers=header)

        try:
            path = search_response.json()['data'][0]
        except IndexError:  # if no flights were found
            print(f"No direct flights were found for {dest}.")
            return None

        # saving the returning data to a new class, to use
        flight_data = FlightData(
            city_from=path['route'][0]['cityFrom'],
            from_airport=path['route'][0]['flyFrom'],
            city_to=path['route'][0]['cityTo'],
            to_airport=path['route'][0]['flyTo'],
            price=path['price'],
            out_date=path['route'][0]['local_departure'].split("T")[0],
            return_date=path['route'][0]['local_departure'].split("T")[0],
            stop_overs=0,
            via_city="",
        )

        # printing the city and price on console and returning it to main.py as well
        print(f"{flight_data.city_to}: £{flight_data.price}")
        return flight_data

    def search_with_one_stop(self, dest):
        self.search_para["max_stopovers"] = 1
        search_response = requests.get(url=self.search_endpoint, params=self.search_para, headers=header)
        try:
            path = search_response.json()['data'][0]
        except IndexError:  # if no flights were found
            print(f"No flights found for {dest}, with one stop.")
            return None

        # saving the returning data to a new class, to use
        flight_data = FlightData(
            city_from=path['route'][0]['cityFrom'],
            from_airport=path['route'][0]['flyFrom'],
            city_to=path['route'][1]['cityTo'],
            to_airport=path['route'][1]['flyTo'],
            price=path['price'],
            out_date=path['route'][0]['local_departure'].split("T")[0],
            return_date=path['route'][2]['local_departure'].split("T")[0],
            stop_overs=1,
            via_city=path["route"][0]["cityTo"],
        )

        print(f"{flight_data.city_to}: £{flight_data.price}")
        return flight_data
