from pydantic import BaseModel
from typing import Dict, Optional

class StatusUpdate(BaseModel):
    """Model for status update entity"""
    id: str
    creation: int # creation timestamp
    status: str
    description: str
    iventory_item: Dict[str, any]

    class Config:
        orm_mode = True
