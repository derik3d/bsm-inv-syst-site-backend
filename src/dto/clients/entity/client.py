from pydantic import BaseModel

class Client(BaseModel):
    id: str
    name: str
    phone: str
    email: str
