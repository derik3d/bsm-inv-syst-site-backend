"""

an status update, it traces an order status and stores the point in time of an order

"""

from pydantic import BaseModel
from typing import Dict, List, Optional

class StatusUpdate(BaseModel):
    """Model for status update entity"""
    #---------------------------------------
    id: str
    creation: int # creation timestamp

    #---------------------------------------
    status: str
    description: str

    #---------------------------------------
    order_data: Dict[str, any]

    class Config:
        orm_mode = True
