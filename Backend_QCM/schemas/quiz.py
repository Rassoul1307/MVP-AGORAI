from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuizBase(BaseModel):
    titre: str
    description: Optional[str] = None
    domain_id: int

class QuizCreate(QuizBase):
    pass

class QuizRead(QuizBase):
    id: int
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True
