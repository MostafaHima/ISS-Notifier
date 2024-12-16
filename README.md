# ISS Tracker

ISS Tracker is a Python application that monitors the location of the International Space Station (ISS) and checks if it is near a specified location during nighttime. It utilizes the `requests` library to interact with the `api.open-notify.org` API for ISS location data.

## Features

- Tracks the real-time location of the ISS.
- Determines if the ISS is near your location (latitude/longitude).
- Verifies whether it is nighttime at your location using sunrise and sunset data.
- Sends notifications when the ISS is visible.

## Requirements

- Python 3.10+
- Libraries: 
  - `requests`
  - `datetime`
  - `time`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MostafaHima/iss-tracker.git
   cd iss-tracker
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## How It Works

1. The application fetches the ISS location using the API endpoint:
   ```
   http://api.open-notify.org/iss-now.json
   ```

2. Your location is compared to the ISS location based on latitude and longitude.
3. It checks if it is nighttime at your location by comparing the current time with sunrise and sunset times (can be fetched using additional APIs like [Sunrise-Sunset API](https://sunrise-sunset.org/api)).
4. Sends a notification if the ISS is visible.

## Example Output

```plaintext
ISS is near your location! Look up at the sky!
```

## Known Issues

- The API `api.open-notify.org` may occasionally time out. Retry logic is implemented to handle this.
- Network issues can prevent the script from running properly.

