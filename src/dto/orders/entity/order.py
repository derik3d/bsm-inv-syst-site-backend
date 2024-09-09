from pydantic import BaseModel

class Order(BaseModel):
    id: str
    client: str
    product: str
    quantity: int
    state: str
