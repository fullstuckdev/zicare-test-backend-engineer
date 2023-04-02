from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from model.schemas import DoctorSchema, Request, Response, RequestDoctor
from API import doctor

doctor_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@doctor_router.post("/")
async def create_doctor_service(request: RequestDoctor, db: Session = Depends(get_db)):
    doctor.create_doctor(db, doctor=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Doctor created successfully").dict(exclude_none=True)

@doctor_router.get("/")
async def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _doctors = doctor.get_doctor(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_doctors)


@doctor_router.get("/{id}")
async def get_doctor_by_id(id: int, db: Session = Depends(get_db)):
    _doctors = doctor.get_doctor_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_doctors)


@doctor_router.patch("/{id}")
async def update_doctor(id: int, request: RequestDoctor, db: Session = Depends(get_db)):
    doctors = id
    _doctor = doctor.update_doctor(db, id=doctors,
                             name=request.parameter.name, age=request.parameter.age,
                             gender=request.parameter.gender,
                             specialization=request.parameter.specialization,
                             contact_number=request.parameter.contact_number)
    return Response(status="Ok", code="200", message="Success update data", result=_doctor)


@doctor_router.delete("/{id}")
async def delete_doctor(id: int,  db: Session = Depends(get_db)):
    doctor.remove_doctor(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)