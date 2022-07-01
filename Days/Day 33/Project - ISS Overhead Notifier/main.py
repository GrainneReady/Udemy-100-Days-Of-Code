import requests
from datetime import datetime
import smtplib
import time

SENDER_EMAIL = "fakeEmail123@thisisfake.com"
SENDER_PASSWORD = "fakePasswordForFakeAccount...qwerty?"
RECIPIENT_EMAIL = "fakeEmail456@thisisfake.com"
MY_LAT = 53.349804  # Your latitude
MY_LONG = -6.260310  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(iss_latitude)
print(iss_longitude)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        if time_now.hour > sunset or time_now.hour < sunrise:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()  # Transport Layer Security - Encrypt email, secures line
                connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIPIENT_EMAIL, msg="Subject:ISS Overhead!\n\nLook up ☝!")
