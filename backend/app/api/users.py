"""User registration and authentication endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserOut, Token, Login
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_verification_token,
    decode_token,
)
from app.core.database import SessionLocal
from app.core.config import get_settings
from app.models.user import User
from sqlalchemy.orm import Session
import os

router = APIRouter()
settings = get_settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOut)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user and emit a verification token to a dev-only file."""
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        if not existing.is_active:
            existing.is_active = True
            db.add(existing)
            db.commit()
            db.refresh(existing)
        return existing
    hashed = get_password_hash(user_in.password)
    # Respect feature flag: require email verification or activate immediately
    user = User(
        email=user_in.email,
        hashed_password=hashed,
        full_name=user_in.full_name,
        is_active=not settings.REQUIRE_EMAIL_VERIFICATION,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # If verification is required, generate and persist a token in dev-only file for retrieval.
    if settings.REQUIRE_EMAIL_VERIFICATION:
        try:
            token = create_verification_token(subject=str(user.id))
            out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "tmp")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"verification_{user.id}.token")
            with open(out_path, "w") as f:
                f.write(token)
            print(f"Verification token for user {user.email} written to: {out_path}")
        except Exception:
            # Fail silently for token write errors — registration succeeded regardless
            pass

    return user


@router.post("/login", response_model=Token)
def login(user_in: Login, db: Session = Depends(get_db)):
    """Authenticate user; require account to be active (verified)."""
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not user.is_active:
        # Account not active (not verified)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account not active. Please verify your email before logging in.",
        )
    token = create_access_token(subject=str(user.id))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/verify")
def verify_account(token: str, db: Session = Depends(get_db)):
    """Verify a newly registered user's email using a token."""
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub"))
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user.is_active:
        return {"status": "already_verified"}

    user.is_active = True
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"status": "verified"}
