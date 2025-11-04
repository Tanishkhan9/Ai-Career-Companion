from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional, List

class ResumeOut(BaseModel):
    id: int
    filename: str
    content_type: Optional[str]
    skills: List[str] = []

    model_config = ConfigDict(from_attributes=True)


