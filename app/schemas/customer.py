from pydantic import BaseModel, ConfigDict
from typing import List
from .factor import FactorOut

class CustomerBase(BaseModel):
    username: str

class CustomerCreate(CustomerBase):
    password: str 

class CustomerOut(CustomerBase):
    id: int
    factors: List[FactorOut] = []
    
    model_config = ConfigDict(from_attributes=True)