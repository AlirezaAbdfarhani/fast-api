from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Factor(Base):
    __tablename__ = 'factors'

    id = Column(Integer, primary_key=True, index=True)
    cid = Column(Integer, ForeignKey('customers.id'))
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(Integer, default=0)
    jalalilate = Column(String, default="")

    customer = relationship("Customer", back_populates="factors")
    items = relationship("FactorItem", back_populates="factor", cascade="all, delete-orphan")