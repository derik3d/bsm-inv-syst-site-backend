"""
An order represents a -bundle of items- to be delivered to a -client-
it traces the orders -state-

"""

from typing import Any, Dict, Optional, List
from pydantic import BaseModel

from model.orders.entity.inventory_item import InventoryItem
from model.orders.entity.status_update import StatusUpdate

class Order(BaseModel):
    """represents a product order for a client"""
    
    #---------------------------------------
    id: str
    creation: float # timestamp
    updated: float # timestamp

    #---------------------------------------

    #state trace
    status: Optional[StatusUpdate]
    status_trace: Optional[List[StatusUpdate]] = []

    #---------------------------------------

    #client
    client_info: Dict[str, Any]

    #inventory
    inventory_items :  Optional[List[InventoryItem]] = []

    class Config:
        orm_mode = True