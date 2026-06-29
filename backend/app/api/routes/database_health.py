from fastapi import APIRouter, HTTPException, status

from app.database.database import test_database_connection


router = APIRouter()


@router.get("/database")
def check_database_connection():
    try:
        database_info = test_database_connection()

        return {
            "status": "connected",
            "message": "Kết nối Supabase thành công",
            "database": database_info,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Không thể kết nối Supabase: {exc}",
        ) from exc