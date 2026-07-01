from pydantic import BaseModel


class VehicleCreate(BaseModel):
    license_plate: str
    owner_name: str | None = None
    owner_phone: str | None = None
    telegram_chat_id: str | None = None


class VehicleResponse(BaseModel):
    id: int
    license_plate: str
    owner_name: str | None = None
    owner_phone: str | None = None
    telegram_chat_id: str | None = None

    class Config:
        from_attributes = True