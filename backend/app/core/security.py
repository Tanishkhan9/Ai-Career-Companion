from datetime import datetime, timedelta, UTC
from typing import Optional
import jwt
from passlib.context import CryptContext
from app.core.config import get_settings

settings = get_settings()

# Use a safe, pure-Python-compatible default hashing scheme for tests and environments
# that may not have a native bcrypt backend installed. pbkdf2_sha256 is widely supported.
pwd_context = CryptContext(schemes=["pbkdf2_sha256", "bcrypt"], deprecated="auto")
JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = "HS256"

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": subject}
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def create_verification_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """Create a short-lived token used for email verification."""
    # default to 24 hours for verification tokens
    expire = timedelta(hours=24) if expires_delta is None else expires_delta
    return create_access_token(subject=subject, expires_delta=expire)


def decode_token(token: str) -> dict:
    """Decode and verify a JWT, raising jwt exceptions on failure."""
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
