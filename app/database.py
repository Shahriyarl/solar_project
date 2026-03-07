from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

import sqlite3

conn = sqlite3.connect("solar.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy (
    time INTEGER,
    solar REAL,
    battery REAL
)
""")

conn.commit()


def save_data(time, solar, battery):

    cursor.execute(
        "INSERT INTO energy VALUES (?, ?, ?)",
        (time, solar, battery)
    )

    conn.commit()


engine = create_engine("sqlite:///solar.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class SolarData(Base):
    __tablename__ = "solar_data"

    id = Column(Integer, primary_key=True)
    hour = Column(Integer)
    solar_power = Column(Float)
    battery = Column(Float)
    load = Column(Float)

Base.metadata.create_all(engine)
