from sqlalchemy.orm import Session
from model.models import Patient
from model.schemas import PatientSchema


def get_patient(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()


def get_patient_by_id(db: Session, id: int):
    return db.query(Patient).filter(Patient.id == id).first()


def create_patient(db: Session, patient: PatientSchema):
    _patient = Patient(name=patient.name, age=patient.age, gender=patient.gender, contact_number=patient.contact_number)
    db.add(_patient)
    db.commit()
    db.refresh(_patient)
    return _patient


def remove_patient(db: Session, id: int):
    _patient = get_patient_by_id(db=db, id=id)
    db.delete(_patient)
    db.commit()


def update_patient(db: Session, id: int, name: str, age: int, gender: str, contact_number: str):
    _patient = get_patient_by_id(db=db, id=id)

    _patient.name = name
    _patient.age = age
    _patient.gender = gender
    _patient.contact_number = contact_number

    db.commit()
    db.refresh(_patient)
    return _patient
