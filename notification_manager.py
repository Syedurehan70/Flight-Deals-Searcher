import smtplib
import os

MY_EMAIL = os.environ.get("my_email")
PASSWORD = os.environ.get("my_pass")
RECEIVERS_EMAIL = os.environ.get("receivers_email")


class NotificationManager:

    # This class is responsible for sending notifications with the deal flight details.
    def send_mail(self, data, price, depart_city, depart_city_air, arrival_city, arrival_city_air, out_date,
                  in_date, stop_overs, via_city):

        # builts a connection between email and email provider's server
        with smtplib.SMTP("smtp.gmail.com") as connection:

            # securing the connection we built, by transport layer security
            connection.starttls()

            # logging in
            connection.login(user=MY_EMAIL, password=PASSWORD)
            if stop_overs == 0:
                message = f"Subject:Low Price Alert! \n\nOnly {price}GBP to fly from {depart_city}-{depart_city_air} to {arrival_city}-{arrival_city_air}" \
                          f", from {out_date} to {in_date}."
                # sending mail, before \n\n there's a  subject and after there is a body of code
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=RECEIVERS_EMAIL,
                                    msg=message)
            else:
                message = f"Subject:Low Price Alert! \n\nOnly {price}GBP to fly from {depart_city}-{depart_city_air}" \
                          f" to {arrival_city}-{arrival_city_air}, from {out_date} to {in_date}.\n\n Flight has" \
                          f" {stop_overs} stop over, via {via_city} City"

                # sending mail, before \n\n there's a  subject and after there is a body of code
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=RECEIVERS_EMAIL,
                                    msg=message)
