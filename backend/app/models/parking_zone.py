from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class ParkingZone(Base):
    __tablename__ = "parking_zones"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    camera_id: Mapped[int] = mapped_column(ForeignKey("cameras.id"))
    name: Mapped[str] = mapped_column(String(100))
    zone_type: Mapped[str] = mapped_column(String(50), default="no_parking")
    points: Mapped[dict] = mapped_column(JSON)
    max_parking_seconds: Mapped[int] = mapped_column(default=60)
    status: Mapped[str] = mapped_column(String(20), default="active")

    camera = relationship("Camera", back_populates="parking_zones")
    violations = relationship("Violation", back_populates="zone")