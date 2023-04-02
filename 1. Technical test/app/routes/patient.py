from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from model.schemas import PatientSchema, Request, Response, RequestPatient
from API import patient

patient_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@patient_router.post("/")
async def create_patient_service(request: RequestPatient, db: Session = Depends(get_db)):
    patient.create_patient(db, patient=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Patient created successfully").dict(exclude_none=True)


@patient_router.get("/")
async def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = patient.get_patient(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)


@patient_router.get("/{id}")
async def get_patient_by_id(id: int, db: Session = Depends(get_db)):
    _patients = patient.get_patient_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_patients)


@patient_router.patch("/{id}")
async def update_patients(id: int, request: RequestPatient, db: Session = Depends(get_db)):
    patients = id
    _patient = patient.update_patient(db, id=patients,
                             name=request.parameter.name, age=request.parameter.age,
                             gender=request.parameter.gender,
                             contact_number=request.parameter.contact_number)
    return Response(status="Ok", code="200", message="Success update data", result=_patient)


@patient_router.delete("/{id}")
async def delete_patient(id: int,  db: Session = Depends(get_db)):
    patient.remove_patient(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)