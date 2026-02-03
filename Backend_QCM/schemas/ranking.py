from pydantic import BaseModel

class RankingBase(BaseModel):
    score_total: int
    position: int

class RankingCreate(RankingBase):
    user_id: int

class RankingRead(RankingBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
