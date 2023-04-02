from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from model.schemas import ScheduleSchema, Request, Response, RequestSchedule
from API import schedule

schedule_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@schedule_router.post("/")
async def create_schedule_service(request: RequestSchedule, db: Session = Depends(get_db)):
    schedule.create_schedule(db, schedule=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Schedule created successfully").dict(exclude_none=True)

@schedule_router.get("/")
async def get_schedule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _schedules = schedule.get_schedule(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_schedules)

@schedule_router.get("/{id}")
async def get_schedule_by_id(id: int, db: Session = Depends(get_db)):
    _schedules = schedule.get_schedule_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_schedules)

@schedule_router.patch("/{id}")
async def update_schedule(id: int, request: RequestSchedule, db: Session = Depends(get_db)):
    schedules = id
    _schedule = schedule.update_schedule(db, id=schedules,
                             clinic_id=request.parameter.clinic_id, doctor_id=request.parameter.doctor_id,
                             start_time=request.parameter.start_time,
                             end_time=request.parameter.end_time)
    return Response(status="Ok", code="200", message="Success update data", result=_schedule)


@schedule_router.delete("/{id}")
async def delete_schedule(id: int,  db: Session = Depends(get_db)):
    schedule.remove_schedule(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)