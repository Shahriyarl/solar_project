from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.solar import get_solar_power
from app.battery import Battery
from app.controller import control_load
from app.database import SessionLocal, SolarData

import datetime

app = FastAPI()

battery = Battery()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# static fayllar
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.get("/status")
def status():
    return {
        "solar_power": 300,
        "battery_level": 50,
        "load": "ON"
    }


@app.get("/history")
def history():
    db = SessionLocal()
    data = db.query(SolarData).order_by(SolarData.id.desc()).limit(50).all()
    db.close()

    return [
        {
            "hour": d.hour,
            "solar": d.solar_power,
            "battery": d.battery,
            "load": d.load
        }
        for d in data
    ]