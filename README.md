# Live Weather Forecast

A Flask-based weather application that fetches **real-time city weather data from the OpenWeatherMap API** and renders the result in a simple web interface.

## Features

- Search weather by city name
- Real-time OpenWeatherMap API requests
- Temperature in Celsius
- Weather condition data
- Humidity and wind information from the API response
- Error handling for invalid or unknown cities
- Flask-rendered frontend

## Tech Stack

- Python
- Flask
- Requests
- OpenWeatherMap API
- HTML / CSS

## Architecture

```text
Browser
   │
   ▼
Flask route
   │
   ▼
City query
   │
   ▼
OpenWeatherMap API
   │
   ▼
JSON weather response
   │
   ▼
Flask template
   │
   ▼
Rendered weather page
```

## Project Structure

```text
Live-Weather-Forecast/
├── app.py
├── templates/
│   └── index.html
├── static/
├── tests/
├── weather/
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Sankalp-gupta1/Live-Weather-Forecast.git
cd Live-Weather-Forecast
```

Install dependencies:

```bash
pip install flask requests
```

## API Configuration

The app requires an OpenWeatherMap API key.

The current source contains an API-key value directly in `app.py`. For normal development or deployment, move the key to an environment variable instead of committing it in source control.

Recommended pattern:

```python
import os
API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

## Run

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Enter a city name to request the current weather.

## Error Handling

If the city is missing or the API does not return a successful response, the UI displays a user-friendly error message instead of weather data.

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
