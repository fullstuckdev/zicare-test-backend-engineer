from sqlalchemy.orm import Session
from model.models import Reservation
from model.schemas import ReservationSchema
from datetime import datetime

def get_reservation(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reservation).offset(skip).limit(limit).all()


def get_reservation_by_id(db: Session, id: int):
    return db.query(Reservation).filter(Reservation.id == id).first()

def create_reservation(db: Session, reservation: ReservationSchema):
    _reservation = Reservation(patient_id=reservation.patient_id, schedule_id=reservation.schedule_id, date=reservation.date, queue_number=reservation.queue_number)
    db.add(_reservation)
    db.commit()
    db.refresh(_reservation)
    return _reservation

def remove_reservation(db: Session, id: int):
    _reservation = get_reservation_by_id(db=db, id=id)
    db.delete(_reservation)
    db.commit()


def update_reservation(db: Session, id: int, patient_id: int, schedule_id: int, date: datetime, queue_number: int):
    _reservation = get_reservation_by_id(db=db, id=id)

    _reservation.patient_id = patient_id
    _reservation.schedule_id = schedule_id
    _reservation.date = date
    _reservation.queue_number = queue_number

    db.commit()
    db.refresh(_reservation)
    return _reservation
