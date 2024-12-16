import requests
import os
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv

load_dotenv()
# API Endpoints and Coordinates
URL = "https://api.sunrise-sunset.org/json"
LAT = 31.000898  # Your latitude
LONG = 29.76258  # Your longitude
MY_EMAIL = os.getenv("MY_EMAIL")  # Your email address
MY_PASSWORD = os.getenv("MY_PASSWORD") # Your email password (use app-specific passwords for security)
TO_EMAIL = os.getenv("TO_EMAIL")

# Function to check if the ISS is near the specified location
def check_location():
    # Fetch ISS current location
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()["iss_position"]
    data_iss_lat = float(data_iss["latitude"])
    data_iss_long = float(data_iss["longitude"])

    # Check if the ISS is within 5 degrees of the specified location
    if abs(data_iss_lat - LAT) <= 5 and abs(data_iss_long - LONG) <= 5:
        return True
    return False

# Function to check if it is nighttime at the specified location
def check_night():
    # Define parameters for sunrise-sunset API
    parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": 0
    }

    # Fetch sunrise and sunset times
    response = requests.get(URL, params=parameters)
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Check if the current time is before sunrise or after sunset
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

# Main loop to continuously monitor the ISS and nighttime status
while True:
    # Check both ISS location and nighttime condition
    if check_location() and check_night():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)  # Log in to email

            # Send email notification
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject: Look Up Satellite Pass Now\n\n"
                    "Hello Mustafa, The ISS is passing over your location now. Look up and enjoy!"
            )
        print("Notification sent.")
    else:
        print("Waiting... Conditions not met yet.")

    # Wait for 60 seconds before checking again
    time.sleep(60)
    continue




