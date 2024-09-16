"""

reprecents an unique type of product on the inventory, each inventory item
must have a serial number in order to be singular adn traceable

"""

from bson import ObjectId
from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict, Optional

class InventoryItem(BaseModel):
    """Model for inventory item entity"""
    
    #---------------------------------------
    id: Optional[str] = Field(default_factory=ObjectId, alias="_id")
    creation: float # timestamp
    
    #---------------------------------------
    #the product description
    product_id: int # specific product reference
    product_name: str # specific product reference name

    # unique identifier for that product inventory item
    serial_number: str

    # any important data to store
    additional_info: Optional[Dict[str, Any]]

    #---------------------------------------

    # try to have up to date order data, an inventory item just have one order
    order_info: Optional[str] = None


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
