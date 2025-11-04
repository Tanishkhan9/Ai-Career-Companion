"""Resume endpoints"""
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Header
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import decode_token
from app.models.resume import Resume
from app.schemas.resume import ResumeOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user_id(authorization: Optional[str] = Header(None)) -> Optional[int]:
    if not authorization or not authorization.lower().startswith("bearer "):
        return None
    token = authorization.split(" ", 1)[1]
    try:
        payload = decode_token(token)
        return int(payload.get("sub"))
    except Exception:
        return None

@router.post("/upload", response_model=ResumeOut)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: Optional[int] = Depends(get_current_user_id),
) -> ResumeOut:
    """
    Upload and parse a resume file
    """
    try:
        # Read file content
        content = await file.read()

        # Naive text extraction (best-effort UTF-8); real parsing would handle PDFs/Docs
        text = None
        try:
            text = content.decode('utf-8', errors='ignore')
        except Exception:
            text = None

        # Very basic skill keyword detection
        keywords = [
            'python','fastapi','react','typescript','javascript','node','sql','postgres','redis','docker','kubernetes','aws','gcp','azure'
        ]
        found: List[str] = []
        haystack = (text or '').lower()
        for k in keywords:
            if k in haystack:
                found.append(k.capitalize())

        resume = Resume(
            user_id=user_id,
            filename=file.filename,
            content_type=file.content_type,
            extracted_text=text,
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)

        return ResumeOut(
            id=resume.id,
            filename=resume.filename,
            content_type=resume.content_type,
            skills=found,
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to process resume: {str(e)}"
        )