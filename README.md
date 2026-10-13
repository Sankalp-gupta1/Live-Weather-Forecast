# Live Weather Forecast

A clean real-time weather application with a Flask reference implementation and a production browser version.

## Live app

**https://live-weather-forecast-sankalp.vercel.app/**

## What changed for deployment

The original Flask app used OpenWeatherMap and required an API key.

For the public deployment I added a separate `web/` version that uses **Open-Meteo**, which provides weather and geocoding data without an API key.

This keeps the original Flask project in the repository while making the live portfolio version easy to open and use.

## Live features

- Search any city
- Current temperature
- Weather condition
- Feels-like temperature
- Humidity
- Wind speed
- Precipitation
- Seven-day forecast
- Rain probability
- Optional browser location
- Mobile responsive UI
- No login
- No database
- No secret key required

## Project structure

```text
Live-Weather-Forecast/
├── app.py                 # original Flask version
├── templates/
├── static/
├── tests/
├── weather/
└── web/
    └── index.html         # deployed production version
```

## Run the deployed web version locally

```bash
cd web
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Run the original Flask version

Install dependencies used by the original app and set your OpenWeatherMap key through an environment variable instead of committing a real secret.

```bash
python app.py
```

## Deployment

The `web/` folder is linked to Vercel. Every push to `main` automatically creates a new deployment.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1  
LinkedIn: https://www.linkedin.com/in/sankalp-gupta-rishi-8617302b0/
