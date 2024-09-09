from pydantic import BaseModel

class Order(BaseModel):
    """represents a product order for a client"""
    id: str
    client: str
    product: str
    quantity: int
    state: str
