# +-------------------------------------------+
# |                Section 33                 |
# +-------------------------------------------+
# | Application Programming Interfaces (APIs) |
# +-------------------------------------------+

# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects
#   that programmers can use to create software or interact with an external system
# Think of it like a barrier between your program and an external system, you're trying to use the rules
#   that the API has described to make a request to the external system for some piece of data
# If the request through the API is valid (done correctly) the External System will make a response
#   through the API with the Data requested

# API Endpoint - Imagine it as a location where the data we need is stored
#   It's usually a URL, coinbase is 'api.coinbase.com', location where data can be found
#   International Space Station Current Location: http://api.open-notify.org/iss-now.json

import requests
from datetime import datetime
# https://pypi.org/project/requests/

# response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get response code
# 1XX - Hold on                 (Informational)
# 2XX - Success, here you go    (Success)
# 3XX - No Permission, go away  (Redirection)
# 4XX - Error, you screwed up   (Client Error)
# 5XX - The server screwed up   (Server Error)
# response.raise_for_status()

# longitude = response.json()["iss_position"]["longitude"]  # Get json using API and get the longitude of the current iss_position
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# API Requests can also have parameters

# Sunrise and Sunset API
#   sunrise-sunset.org/api

# CHALLENGE: Modify the API call: turn of the formatting and time in the 24-hour style ✔
DUBLIN_LATITUDE = 53.349804
DUBLIN_LONGITUDE = -6.260310
parameters = {
    "lat": DUBLIN_LATITUDE,
    "lng": DUBLIN_LONGITUDE,
    "formatted": 0  # If set to 1, Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # Get hour of sunrise in terms of 24hr clock
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
