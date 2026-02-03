from pydantic import BaseModel

class ChoiceBase(BaseModel):
    contenu: str
    is_correct: bool = False

class ChoiceCreate(ChoiceBase):
    question_id: int

class ChoiceRead(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True
