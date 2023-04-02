from sqlalchemy.orm import Session
from model.models import Clinic
from model.schemas import ClinicSchema

def get_clinic(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Clinic).offset(skip).limit(limit).all()


def get_clinic_by_id(db: Session, id: int):
    return db.query(Clinic).filter(Clinic.id == id).first()

def create_clinic(db: Session, clinic: ClinicSchema):
    _clinic = Clinic(name=clinic.name, address=clinic.address, contact_number=clinic.contact_number)
    db.add(_clinic)
    db.commit()
    db.refresh(_clinic)
    return _clinic

def remove_clinic(db: Session, id: int):
    _clinic = get_clinic_by_id(db=db, id=id)
    db.delete(_clinic)
    db.commit()


def update_clinic(db: Session, id: int, name: str, address: str, contact_number: str):
    _clinic = get_clinic_by_id(db=db, id=id)

    _clinic.name = name
    _clinic.address = address
    _clinic.contact_number = contact_number

    db.commit()
    db.refresh(_clinic)
    return _clinic
