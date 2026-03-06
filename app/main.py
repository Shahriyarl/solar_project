from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.solar import SolarSystem
from app.solar import get_solar_power
from app.battery import Battery
from app.controller import control_load
from app.database import SessionLocal, SolarData

import datetime
import time
import random




app = FastAPI()

system = SolarSystem()

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

    system.update()

    return {
        "solar_power": system.solar_power,
        "battery_level": system.battery_level,
        "load": system.load
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