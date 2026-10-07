from pydantic import BaseModel, ConfigDict

class FactorItemBase(BaseModel):
    product_id: int
    no: int

class FactorItemCreate(FactorItemBase):
    pass 

class FactorItemOut(FactorItemBase):
    id: int
    factor_id: int
    fee: int
    sum_fee: int
    
    model_config = ConfigDict(from_attributes=True)