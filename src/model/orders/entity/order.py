from pydantic import BaseModel

class Order(BaseModel):
    """represents a product order for a client"""
    id: str
    client_id: str
    product_id: str
    quantity: int
    state: str

    class Config:
        orm_mode = True