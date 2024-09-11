from pydantic import BaseModel
from typing import Optional

class ProductType(BaseModel):
    """Model for product type entity"""
    id: int
    type_name: str
    nemo: str
    parent_type_id: Optional[int] = None

    class Config:
        orm_mode = True
