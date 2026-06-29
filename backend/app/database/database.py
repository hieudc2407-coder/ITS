from collections.abc import Generator

from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=3,
    max_overflow=2,
    connect_args={
        "sslmode": "require",
    },
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    """
    Tạo database session cho mỗi request FastAPI.
    Session sẽ tự đóng khi request kết thúc.
    """
    database_session = SessionLocal()

    try:
        yield database_session
    finally:
        database_session.close()


def test_database_connection() -> dict:
    """
    Kiểm tra kết nối đến Supabase PostgreSQL.
    """
    with engine.connect() as connection:
        result = connection.execute(
            text(
                """
                SELECT
                    current_database() AS database_name,
                    current_user AS database_user,
                    NOW() AS database_time
                """
            )
        ).mappings().one()

        return {
            "database_name": result["database_name"],
            "database_user": result["database_user"],
            "database_time": result["database_time"],
        }