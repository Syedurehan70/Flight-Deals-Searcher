# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
# from pprint import pprint
import datetime as dt


# generating date for tom and after 6 months.
now = dt.datetime.now()
tomorrow = now + dt.timedelta(days=1)
six_months = tomorrow + dt.timedelta(days=6*30)

tom_date = tomorrow.strftime("%d/%m/%Y")
six_months_date = six_months.strftime("%d/%m/%Y")

# object initializing
d_manage = DataManager()
flight_search = FlightSearch()
notify = NotificationManager()

# calling method, getting data from connected sheet
data = d_manage.get()

# for every dict in data list, this loop runs
for code in data:
    if code['iataCode'] == "":

        # for empty iata code place, fill it with iatacode for the location
        code['iataCode'] = flight_search.get_destination_code(name=code['city'])

        # put it in on sheet, by using row id
        d_manage.test(iata=code['iataCode'], id=code['id'])


# for every row data in (updated) data, search flights
for i in data:
    flight = flight_search.search_with_zero_stops(dest=i['iataCode'], tom=tom_date, to=six_months_date)

    if flight is not None:
        if i['lowestPrice'] > flight.price:
            notify.send_mail(data=data,
                             price=flight.price,
                             depart_city=flight.city_from,
                             depart_city_air=flight.from_airport,
                             arrival_city=flight.city_to,
                             arrival_city_air=flight.to_airport,
                             out_date=flight.out_date,
                             in_date=flight.return_date,
                             stop_overs=flight.stop_overs,
                             via_city=flight.via_city)

    else:
        stop_over_flight = flight_search.search_with_one_stop(dest=i['iataCode'])

        if stop_over_flight is not None:
            if i['lowestPrice'] > stop_over_flight.price:
                notify.send_mail(data=data,
                                 price=stop_over_flight.price,
                                 depart_city=stop_over_flight.city_from,
                                 depart_city_air=stop_over_flight.from_airport,
                                 arrival_city=stop_over_flight.city_to,
                                 arrival_city_air=stop_over_flight.to_airport,
                                 out_date=stop_over_flight.out_date,
                                 in_date=stop_over_flight.return_date,
                                 stop_overs=stop_over_flight.stop_overs,
                                 via_city=stop_over_flight.via_city)

