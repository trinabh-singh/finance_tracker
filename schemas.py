from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: str
    category: str
    date: date
    notes: Optional[str] = None


class RecordResponse(RecordCreate):
    id: int

    class Config:
        from_attributes = True