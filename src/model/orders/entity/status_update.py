from pydantic import BaseModel, Field, field_validator
from bson import ObjectId
from typing import Optional

class StatusUpdate(BaseModel):
    """Model for status update entity"""
    
    id: Optional[str] = Field(default_factory=ObjectId, alias="_id")
    creation: float  # creation timestamp
    status: str
    description: str
    order_info: str


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
        arbitrary_types_allowed = True
