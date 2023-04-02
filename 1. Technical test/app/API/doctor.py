from sqlalchemy.orm import Session
from model.models import Doctor
from model.schemas import DoctorSchema


def get_doctor(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Doctor).offset(skip).limit(limit).all()


def get_doctor_by_id(db: Session, id: int):
    return db.query(Doctor).filter(Doctor.id == id).first()

def create_doctor(db: Session, doctor: DoctorSchema):
    _doctor = Doctor(name=doctor.name, age=doctor.age, gender=doctor.gender, specialization = doctor.specialization, contact_number=doctor.contact_number)
    db.add(_doctor)
    db.commit()
    db.refresh(_doctor)
    return _doctor

def remove_doctor(db: Session, id: int):
    _doctor = get_doctor_by_id(db=db, id=id)
    db.delete(_doctor)
    db.commit()


def update_doctor(db: Session, id: int, name: str, age: int, gender: str, specialization: str, contact_number: str):
    _doctor = get_doctor_by_id(db=db, id=id)

    _doctor.name = name
    _doctor.age = age
    _doctor.gender = gender
    _doctor.specialization = specialization
    _doctor.contact_number = contact_number

    db.commit()
    db.refresh(_doctor)
    return _doctor
