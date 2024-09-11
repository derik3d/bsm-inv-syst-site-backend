from pydantic import BaseModel

class Product(BaseModel):
    """Model for product entity"""
    id: int
    product_name: str
    product_description: str
    fk_product_type_id: int  # Foreign key reference to the product type

    class Config:
        orm_mode = True
