from pathlib import Path
from uuid import uuid4

from supabase import Client, create_client

from app.core.config import settings


supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SECRET_KEY,
)


def upload_violation_image(image_path: str) -> str:
    local_path = Path(image_path)

    if not local_path.exists():
        raise FileNotFoundError(f"Không tìm thấy ảnh: {image_path}")

    storage_path = (
        f"violations/{uuid4().hex}{local_path.suffix.lower()}"
    )

    with local_path.open("rb") as image_file:
        supabase.storage.from_("violation-evidenced").upload(
            path=storage_path,
            file=image_file,
            file_options={
                "content-type": "image/jpeg",
                "upsert": "false",
            },
        )

    return storage_path