from typing import List, Optional, Generic, TypeVar
from datetime import datetime
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class PatientSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None

    class Config:
        orm_mode = True

class RequestPatient(BaseModel):
    parameter: PatientSchema = Field(...)

class DoctorSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    specialization: Optional[str] = None
    contact_number: Optional[str] = None

    class Config:
        orm_mode = True

class RequestDoctor(BaseModel):
    parameter: DoctorSchema = Field(...)

class ReservationSchema(BaseModel):
    id: Optional[int] = None
    patient_id: Optional[int] = None
    schedule_id: Optional[int] = None
    date: Optional[datetime] = None
    queue_number: Optional[int] = None

    class Config:
        orm_mode = True

class RequestReservation(BaseModel):
    parameter: ReservationSchema = Field(...)

class ClinicSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None

    class Config:
        orm_mode = True

class RequestClinic(BaseModel):
    parameter: ClinicSchema = Field(...)

class ScheduleSchema(BaseModel):
    id: Optional[int] = None
    clinic_id: Optional[int] = None
    doctor_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    class Config:
        orm_mode = True

class RequestSchedule(BaseModel):
    parameter: ScheduleSchema = Field(...)

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
