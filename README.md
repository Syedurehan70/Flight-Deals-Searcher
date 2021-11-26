# Flight-Deals-Searcher

This program gives alert on our email, if there is a flight cheaper than the prices we defined in our sheet, to a destination we mentioned, with one or zero step_overs,
and sends us email with necessary alert details.

So first we made a spreadsheet put made some columns and put some name of the cities, and the prices for the flights which goes there, we use SHEETY for this purpose.

data_managaer get_method: After that, we use sheety api, to get the data on the spreadsheet, than extracted the prices column data only, saved it in json format. passes in main.py.

main.py, get_destination_code: than using the data we extracted from the sheet we get the iata codes for the destination cities mentioned in spreadsheet, using kiwi  api in
FlightSearch class method of get_destination_code. we checked if the iatacode column on sheet is empty if yes  than we searched it and putted the code their.

main.py, search_with_zero_stops, search_with_one_stop, : after that we use iatacode and dates of yesterday and six months from there to find flights to the dedstination 
with no step_overs, if found, we extracted the necessary data we need saved them in FlightData, than we compare prize, if it's lower than the ones we've mentioned

than we pass them into notification_manager.py and use it to send an email, if flight with no step_overs were no found we search for the one with one step_over, if still
not found we return the message saying that no flights were found.

in notication_email we mentioned the departure city with airport and arrival city with airport, we've passed the duration of 7 to 28 days, during period of six months as parameters.
