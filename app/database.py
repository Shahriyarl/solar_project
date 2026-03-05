from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

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