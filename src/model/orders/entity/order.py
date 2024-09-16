"""
An order represents a -bundle of items- to be delivered to a -client-
it traces the orders -state-

"""

from typing import Any, Dict, Optional, List
from bson import ObjectId
from pydantic import BaseModel, Field, field_validator

from model.orders.entity.inventory_item import InventoryItem
from model.orders.entity.status_update import StatusUpdate
from model.orders.entity.object_id import PyObjectId


class Order(BaseModel):
    """represents a product order for a client"""
    
    #---------------------------------------
    id: Optional[str] = Field(default_factory=ObjectId, alias="_id")
    creation: float # timestamp
    updated: float # timestamp

    #---------------------------------------

    #state trace
    status: Optional[StatusUpdate]
    status_trace: Optional[List[StatusUpdate]] = []

    #---------------------------------------

    #client
    client: Dict[str, Any]

    #inventory
    inventory_items :  Optional[List[InventoryItem]] = None


    #---------------------------------------

    @field_validator("id", mode="before", check_fields=False)
    def convert_objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed=True