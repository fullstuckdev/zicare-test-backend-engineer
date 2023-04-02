from fastapi import FastAPI
from model import models
from routes.patient import patient_router
from routes.doctor import doctor_router
from routes.clinic import clinic_router
from routes.schedule import schedule_router
from routes.reservation import reservation_router
from config.config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome"

app.include_router(patient_router, prefix="/patient", tags=["patient"])
app.include_router(clinic_router, prefix="/clinic", tags=["clinic"])
app.include_router(schedule_router, prefix="/schedule", tags=["schedule"])
app.include_router(doctor_router, prefix="/doctor", tags=["doctor"])
app.include_router(reservation_router, prefix="/reservation", tags=["reservation"])
