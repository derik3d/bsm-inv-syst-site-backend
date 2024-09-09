from pydantic import BaseModel

class Client(BaseModel):
    """represents a customer and its data"""
    id: str
    name: str
    phone: str
    email: str
