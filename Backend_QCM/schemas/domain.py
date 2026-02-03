from pydantic import BaseModel
from typing import Optional

class DomainBase(BaseModel):
    nom: str
    description: Optional[str] = None
    parent_id: Optional[int] = None
    is_active: bool = True

class DomainCreate(DomainBase):
    pass

class DomainRead(DomainBase):
    id: int

    class Config:
        from_attributes = True
