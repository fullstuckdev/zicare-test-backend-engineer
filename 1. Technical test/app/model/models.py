from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey
from config.config import Base

class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    contact_number = Column(String)

class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    specialization = Column(String)
    contact_number = Column(String)

class Clinic(Base):
    __tablename__ = "clinic"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)

class Schedule(Base):
    __tablename__ = 'schedule'
    
    id = Column(Integer, primary_key=True)
    clinic_id = Column(Integer, ForeignKey('clinic.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    date = Column(DateTime)
    queue_number = Column(Integer)