"""

an status update, it traces an order status and stores the point in time of an order

"""

from pydantic import BaseModel
from typing import Any, Dict

class StatusUpdate(BaseModel):
    """Model for status update entity"""
    #---------------------------------------
    id: str
    creation: float # creation timestamp

    #---------------------------------------
    status: str
    description: str

    #---------------------------------------
    order_info: Dict[str, Any]

    class Config:
        orm_mode = True
