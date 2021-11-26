class FlightData:  # saving all the fetched data to this class to use anywhere in program
    def __init__(self, city_from, from_airport, city_to, to_airport, price, out_date, return_date, stop_overs,
                 via_city):
        self.city_from = city_from
        self.from_airport = from_airport
        self.city_to = city_to
        self.to_airport = to_airport
        self.price = price
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
