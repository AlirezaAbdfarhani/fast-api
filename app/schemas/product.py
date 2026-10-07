
from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    code: str = ""
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)