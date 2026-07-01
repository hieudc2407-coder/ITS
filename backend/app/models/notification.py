from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    violation_id: Mapped[int] = mapped_column(ForeignKey("violations.id"))

    channel: Mapped[str] = mapped_column(String(30), default="telegram")
    receiver: Mapped[str | None] = mapped_column(String(100), nullable=True)
    message: Mapped[str] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(String(30), default="sent")
    sent_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    violation = relationship("Violation", back_populates="notifications")