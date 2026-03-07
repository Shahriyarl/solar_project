from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.controller import system_step
from app.database import save_data, SessionLocal, SolarData

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# frontend statik fayllar
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.get("/status")
def status():
    data = system_step()
    save_data(
        data["hour"],
        data["solar_power"],
        data["battery"]
    )
    return data


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