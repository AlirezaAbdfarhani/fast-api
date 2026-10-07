from sqlalchemy.orm import Session
from app.models.customer_model import Customer
from app.schemas.customer import CustomerCreate
import hashlib

def get_customers(db: Session):
    return db.query(Customer).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def create_customer(db: Session, customer: CustomerCreate):
    hashed_pw = hashlib.sha256(customer.password.encode()).hexdigest()
    db_customer = Customer(username=customer.username, password_hash=hashed_pw)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer_crud(db: Session, customer_id: int, updated_customer: CustomerCreate):
    db_customer = get_customer_by_id(db, customer_id)
    if db_customer:
        db_customer.username = updated_customer.username
        db_customer.password_hash = hashlib.sha256(updated_customer.password.encode()).hexdigest()
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer_crud(db: Session, customer_id: int):
    db_customer = get_customer_by_id(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return True
    return False

def delete_all_customers(db: Session):
    count = db.query(Customer).count()
    db.query(Customer).delete()
    db.commit()
    return count