# Live weather in the terminal
# API: Open-Meteo (free, no API key needed)

import json
import requests

URL = "https://api.open-meteo.com/v1/forecast"

# Change these to your city (this is Karachi)
CITY = "Karachi"
LATITUDE = 24.86
LONGITUDE = 67.01

# The 5 fields we ask the API for
FIELDS = "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code"

# weather_code is a number, so we turn it into words
CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    51: "Light drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    80: "Rain showers",
    95: "Thunderstorm",
}


def get_weather():
    """Call the API and return the 'current' part of the JSON."""
    settings = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": FIELDS,
    }
    response = requests.get(URL, params=settings, timeout=10)
    response.raise_for_status()   # stop if the API returned an error
    return response.json()


def draw(current):
    """Print the weather as a simple box in the terminal."""
    temp = current["temperature_2m"]
    feels = current["apparent_temperature"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    sky = CODES.get(current["weather_code"], "Unknown")

    print("+" + "-" * 34 + "+")
    print("| {:<32} |".format(CITY + " weather"))
    print("+" + "-" * 34 + "+")
    print("| {:<14} {:>17} |".format("Temperature", str(temp) + " C"))
    print("| {:<14} {:>17} |".format("Feels like", str(feels) + " C"))
    print("| {:<14} {:>17} |".format("Humidity", str(humidity) + " %"))
    print("| {:<14} {:>17} |".format("Wind speed", str(wind) + " km/h"))
    print("| {:<14} {:>17} |".format("Sky", sky))
    print("+" + "-" * 34 + "+")

    # a tiny bar chart so you can "see" the humidity
    bars = int(humidity / 5)
    print("\nHumidity bar: " + "#" * bars + "." * (20 - bars))


data = get_weather()

print("=== Raw JSON from the API ===")
print(json.dumps(data["current"], indent=4))

print("\n=== Same data, drawn nicely ===")
draw(data["current"])
