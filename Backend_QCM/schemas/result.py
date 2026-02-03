from pydantic import BaseModel
from datetime import datetime

class ResultBase(BaseModel):
    score: int
    mistakes: int

class ResultCreate(ResultBase):
    quiz_id: int

class ResultRead(ResultBase):
    id: int
    user_id: int
    quiz_id: int
    started_at: datetime
    finished_at: datetime

    class Config:
        from_attributes = True
