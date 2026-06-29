from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Violation(Base):
    __tablename__ = "violations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    vehicle_id: Mapped[int | None] = mapped_column(ForeignKey("vehicles.id"), nullable=True)
    camera_id: Mapped[int] = mapped_column(ForeignKey("cameras.id"))
    zone_id: Mapped[int] = mapped_column(ForeignKey("parking_zones.id"))

    license_plate: Mapped[str | None] = mapped_column(String(20), nullable=True)

    detected_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    violation_started_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[int] = mapped_column(Integer, default=0)

    evidence_image_path: Mapped[str | None] = mapped_column(String(255), nullable=True)

    status: Mapped[str] = mapped_column(String(30), default="pending")
    telegram_sent: Mapped[bool] = mapped_column(default=False)

    vehicle = relationship("Vehicle", back_populates="violations")
    camera = relationship("Camera", back_populates="violations")
    zone = relationship("ParkingZone", back_populates="violations")
    notifications = relationship("Notification", back_populates="violation")