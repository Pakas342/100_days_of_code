import requests
import datetime as dt
import smtplib
import time

SUNRISE_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 4.6406589695490785
MY_LNG = -74.06985854147935
ISS_URL = "http://api.open-notify.org/iss-now.json"
MY_EMAIL = "jcbp1999@gmail.com"
PASSWORD = "cwch ujti nmni lohz"


def iss_above(lat=MY_LAT, lng=MY_LNG):
    iss_response = requests.get(url=ISS_URL)
    iss_response.raise_for_status()
    iss_lat = float(iss_response.json()["iss_position"]["latitude"])
    iss_lng = float(iss_response.json()["iss_position"]["longitude"])
    if abs(iss_lat - lat) < 5 and abs(iss_lng - lng) < 5:
        return True
    else:
        return False


def is_night_time():

    sunrise_parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    sunrise_response = requests.get(url=SUNRISE_URL, params=sunrise_parameters)
    sunrise_response.raise_for_status()
    time_data = sunrise_response.json()
    sunrise_hour = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = int(dt.datetime.now().hour)
    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if iss_above() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject: ISS ABOVE!☝️\n\nLook up! you got the iss above")
    else:
        print("ISS no above")
