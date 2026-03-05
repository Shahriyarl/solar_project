# Virtual Solar Energy Management System

A Python-based simulation of a small solar power station with monitoring dashboard.

## Technologies

- Python
- FastAPI
- SQLite
- Chart.js
- Poetry
- Docker

## Features

- Solar panel power simulation
- Battery storage model
- Load control logic
- Real-time monitoring dashboard
- Historical data visualization

## Run locally

poetry install

poetry run uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

## Docker

docker build -t solar-system .

docker run -p 8000:8000 solar-system