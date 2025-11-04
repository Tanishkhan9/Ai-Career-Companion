"""Database session management"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables automatically (useful for tests and simple setups).
try:
    from app.models.base import Base
    # Import all model modules so they are registered on Base.metadata
    try:
        # individual model imports ensure tables are available
        import app.models.user  # noqa: F401
        import app.models.resume  # noqa: F401
    except Exception:
        pass
    Base.metadata.create_all(bind=engine)
except Exception:
    # In case database isn't available or creation fails during import, ignore here.
    pass