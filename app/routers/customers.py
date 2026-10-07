from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import customer as crud_customer 
from app.schemas.customer import CustomerCreate, CustomerOut

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.get("/", response_model=list[CustomerOut])
def read_customers(db: Session = Depends(get_db)):
    customers = crud_customer.get_customers(db)
    return customers or []

@router.get("/{customer_id}", response_model=CustomerOut)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud_customer.get_customer_by_id(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = crud_customer.create_customer(db=db, customer=customer)
    return new_customer

@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, updated_customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud_customer.update_customer_crud(db, customer_id=customer_id, updated_customer=updated_customer)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = crud_customer.delete_customer_crud(db, customer_id=customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"detail": "Customer deleted successfully"}

@router.delete("/")
def delete_all_customers(db: Session = Depends(get_db)):
    count = crud_customer.delete_all_customers(db)
    return {"detail": f"{count} customers deleted"}