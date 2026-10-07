from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class FactorItem(Base):
    __tablename__ = 'factor_items'

    id = Column(Integer, primary_key=True, index=True)
    factor_id = Column(Integer, ForeignKey('factors.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    no = Column(Integer, default=1)              
    fee = Column(Integer, default=0)             
    sum_fee = Column(Integer, default=0)         

    factor = relationship("Factor", back_populates="items")
    product = relationship("Product", back_populates="items")