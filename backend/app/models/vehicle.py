from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    license_plate: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    owner_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    owner_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    telegram_chat_id: Mapped[str | None] = mapped_column(String(50), nullable=True)

    violations = relationship("Violation", back_populates="vehicle")