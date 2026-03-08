from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./solar.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Energy(Base):
    __tablename__ = "energy"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer)
    solar = Column(Float)
    battery = Column(Float)


Base.metadata.create_all(bind=engine)


def save_data(time, solar, battery):
    db = SessionLocal()

    data = Energy(
        time=time,
        solar=solar,
        battery=battery
    )

    db.add(data)
    db.commit()
    db.close()
