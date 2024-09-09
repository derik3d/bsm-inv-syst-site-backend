from pydantic import BaseModel

class Product(BaseModel):
    """represents a product/service we offer"""
    id: str
    name: str
    description: str
