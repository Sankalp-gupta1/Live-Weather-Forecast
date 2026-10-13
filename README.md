# Live Weather Forecast

A public weather dashboard with a Flask reference backend and a production browser UI.

## Live app

**https://live-weather-forecast.vercel.app/**

The hosted version uses **Open-Meteo**, so it works without an API key and does not expose private credentials.

## Features

- Search weather by city
- Current temperature
- Feels-like temperature
- Humidity
- Wind speed
- Five-day forecast
- Browser geolocation button
- Responsive mobile/desktop UI
- No database
- No API key

## Architecture

### Hosted web app

```text
Browser
  -> Open-Meteo Geocoding API
  -> Open-Meteo Forecast API
  -> Render current conditions + 5-day forecast
```

### Flask reference app

The original Flask application is still included. Its backend was updated to use Open-Meteo as well, removing the previously committed weather API key.

```text
Flask route
  -> geocode city
  -> request current weather
  -> map the response into the original template contract
```

## Run the hosted-style web app locally

```bash
cd web
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Run the Flask version

Install:

```bash
pip install flask requests
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project structure

```text
Live-Weather-Forecast/
├── app.py
├── templates/
├── static/
├── weather/
├── tests/
├── web/
│   └── index.html
└── README.md
```

## Tech stack

- Python
- Flask
- Requests
- HTML
- CSS
- JavaScript
- Open-Meteo
- Vercel

## Security improvement

The old source contained a weather-service key directly in code. The current version no longer needs that key. The hosted and Flask versions use a keyless weather provider.

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
