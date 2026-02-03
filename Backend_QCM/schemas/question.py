from pydantic import BaseModel
from typing import Optional
from enum import Enum

class QuestionType(str, Enum):
    QCM = "QCM"
    TEXTE = "TEXTE"
    VRAI_FAUX = "VRAI_FAUX"

class QuestionBase(BaseModel):
    contenu: str
    niveau: Optional[str] = None
    type: QuestionType
    domain_id: int
    quiz_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    created_by: int

    class Config:
        from_attributes = True
