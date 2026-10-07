from pydantic import BaseModel, ConfigDict, Field
from typing import List
from datetime import datetime
from .factor_item import FactorItemCreate, FactorItemOut


class FactorCreate(BaseModel):
    customer_id: int
    items: List[FactorItemCreate] = []


class FactorOut(BaseModel):
    id: int
    customer_id: int = Field(alias='cid')
    date: datetime
    total: int
    items: List[FactorItemOut] = []

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)