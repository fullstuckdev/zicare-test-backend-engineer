from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from model.schemas import ReservationSchema, Request, Response, RequestReservation
from API import reservation

reservation_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@reservation_router.post("/")
async def create_reservation_service(request: RequestReservation, db: Session = Depends(get_db)):
    reservation.create_reservation(db, reservation=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Reservation created successfully").dict(exclude_none=True)

@reservation_router.get("/")
async def get_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _reservations = reservation.get_reservation(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_reservations)


@reservation_router.get("/{id}")
async def get_reservation_by_id(id: int, db: Session = Depends(get_db)):
    _reservations = reservation.get_reservation_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_reservations)


@reservation_router.patch("/{id}")
async def update_patients(id: int, request: RequestReservation, db: Session = Depends(get_db)):
    reservations = id
    _reservation = reservation.update_reservation(db, id=reservations,
                             patient_id=request.parameter.patient_id, schedule_id=request.parameter.schedule_id,
                             date=request.parameter.date,
                             queue_number=request.parameter.queue_number)
    return Response(status="Ok", code="200", message="Success update data", result=_reservation)


@reservation_router.delete("/{id}")
async def delete_reservation(id: int,  db: Session = Depends(get_db)):
    reservation.remove_reservation(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)