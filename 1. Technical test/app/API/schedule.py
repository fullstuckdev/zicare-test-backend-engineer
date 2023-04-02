from sqlalchemy.orm import Session
from model.models import Schedule
from model.schemas import ScheduleSchema
from datetime import datetime


def get_schedule(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Schedule).offset(skip).limit(limit).all()


def get_schedule_by_id(db: Session, id: int):
    return db.query(Schedule).filter(Schedule.id == id).first()

def create_schedule(db: Session, schedule: ScheduleSchema):
    _schedule = Schedule(clinic_id = schedule.clinic_id, doctor_id = schedule.doctor_id, start_time = schedule.start_time, end_time = schedule.end_time)
    db.add(_schedule)
    db.commit()
    db.refresh(_schedule)
    return _schedule

def remove_schedule(db: Session, id: int):
    _schedule = get_schedule_by_id(db=db, id=id)
    db.delete(_schedule)
    db.commit()


def update_schedule(db: Session, id: int, clinic_id: id, doctor_id: id, start_time: datetime, end_time: datetime):
    _schedule = get_schedule_by_id(db=db, id=id)

    _schedule.clinic_id = clinic_id
    _schedule.doctor_id = doctor_id
    _schedule.start_time = start_time
    _schedule.end_time = end_time

    db.commit()
    db.refresh(_schedule)
    return _schedule
