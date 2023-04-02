from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from model.schemas import ClinicSchema, Request, Response, RequestClinic
from API import clinic

clinic_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@clinic_router.post("/")
async def create_clinic_service(request: RequestClinic, db: Session = Depends(get_db)):
    clinic.create_clinic(db, clinic=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Clinic created successfully").dict(exclude_none=True)

@clinic_router.get("/")
async def get_clinics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _clinics = clinic.get_clinic(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_clinics)


@clinic_router.get("/{id}")
async def get_clinic_by_id(id: int, db: Session = Depends(get_db)):
    _clinics = clinic.get_clinic_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_clinics)

@clinic_router.patch("/{id}")
async def update_clinic(id: int, request: RequestClinic, db: Session = Depends(get_db)):
    clients = id
    _clinic = clinic.update_clinic(db, id=clients,
                             name=request.parameter.name, 
                             address=request.parameter.address,
                             contact_number=request.parameter.contact_number)
    return Response(status="Ok", code="200", message="Success update data", result=_clinic)

@clinic_router.delete("/{id}")
async def delete_client(id: int,  db: Session = Depends(get_db)):
    clinic.remove_clinic(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)