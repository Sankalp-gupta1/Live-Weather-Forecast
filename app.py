from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "rime fog",
    51: "light drizzle",
    53: "drizzle",
    55: "heavy drizzle",
    61: "light rain",
    63: "rain",
    65: "heavy rain",
    71: "light snow",
    73: "snow",
    75: "heavy snow",
    80: "rain showers",
    81: "rain showers",
    82: "heavy rain showers",
    95: "thunderstorm",
    96: "thunderstorm with hail",
    99: "thunderstorm with hail",
}


def get_weather(city):
    """Fetch current weather without storing or exposing an API key."""
    geo = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=10,
    )
    geo.raise_for_status()
    results = geo.json().get("results") or []
    if not results:
        return None

    place = results[0]
    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": "temperature_2m,relative_humidity_2m,weather_code",
            "timezone": "auto",
        },
        timeout=10,
    )
    response.raise_for_status()
    current = response.json().get("current") or {}
    code = current.get("weather_code")

    # Keep the original template contract so the Flask version remains compatible.
    return {
        "name": ", ".join(
            value
            for value in (place.get("name"), place.get("admin1"), place.get("country"))
            if value
        ),
        "main": {
            "temp": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
        },
        "weather": [{"description": WEATHER_CODES.get(code, f"weather code {code}")}],
    }


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", weather_data=None, error=None)


@app.route("/weather", methods=["GET"])
def weather():
    city = (request.args.get("city") or "").strip()
    if not city:
        return render_template(
            "index.html", weather_data=None, error="Please enter a city name."
        )

    try:
        weather_data = get_weather(city)
    except requests.RequestException:
        weather_data = None

    if weather_data:
        return render_template("index.html", weather_data=weather_data, error=None)

    return render_template(
        "index.html",
        weather_data=None,
        error="City not found or weather service unavailable. Please try again.",
    )


if __name__ == "__main__":
    app.run(debug=True)
