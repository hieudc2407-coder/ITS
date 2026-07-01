from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleResponse


router = APIRouter()


@router.post("/vehicles", response_model=VehicleResponse)
def create_vehicle(
    vehicle_data: VehicleCreate,
    db: Session = Depends(get_db),
):
    existing_vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.license_plate == vehicle_data.license_plate)
        .first()
    )

    if existing_vehicle:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Biển số xe đã tồn tại",
        )

    vehicle = Vehicle(
        license_plate=vehicle_data.license_plate,
        owner_name=vehicle_data.owner_name,
        owner_phone=vehicle_data.owner_phone,
        telegram_chat_id=vehicle_data.telegram_chat_id,
    )

    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)

    return vehicle


@router.get("/vehicles", response_model=list[VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).order_by(Vehicle.id.desc()).all()
    return vehicles