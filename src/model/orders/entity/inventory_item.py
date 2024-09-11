from pydantic import BaseModel
from typing import List, Optional

from model.orders.entity.status_update import StatusUpdate

class InventoryItem(BaseModel):
    """Model for inventory item entity"""
    id: str
    product_name: str # specific product reference name
    product_id: int # specific product reference
    serial_number: str # unique identifier for that product inventory item
    additional_info: Optional[object] # any important data to store

    creation: int # timestamp

    status_update: Optional[List[StatusUpdate]] = []

    class Config:
        orm_mode = True
