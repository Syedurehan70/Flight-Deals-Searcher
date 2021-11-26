import requests

get_endpoint = "https://api.sheety.co/8f891c24d63bb92ecb30cffb0711d084/myFlightDeals/prices"


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def get(self):

        # getting data from google sheets and turning it in json format for use, returning to main.py
        get_response = requests.get(url=get_endpoint)
        get_data = get_response.json()['prices']
        return get_data

    def test(self, iata, id):
        # putting the info in sheet

        put_endpoint = f"{get_endpoint}/{int(id)}"
        para = {
            "price": {
                "iataCode": iata,
            }
        }
        put_response = requests.put(url=put_endpoint, json=para)
        put_response.raise_for_status()
