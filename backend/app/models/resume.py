"""Resume model definition"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Resume(BaseModel):
    __tablename__ = "resumes"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=True)
    extracted_text = Column(Text, nullable=True)

    # optional relationship
    user = relationship("User", backref="resumes")


