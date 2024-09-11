"""

reprecents an unique type of product on the inventory, each inventory item
must have a serial number in order to be singular adn traceable

"""

from pydantic import BaseModel
from typing import Any, Dict, Optional

from model.orders.entity.order import Order

class InventoryItem(BaseModel):
    """Model for inventory item entity"""
    
    #---------------------------------------
    id: str
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
    order_info: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
