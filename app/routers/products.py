from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import products as crud_products
from app.schemas import product as schemas

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=list[schemas.ProductOut])
def read_products(db: Session = Depends(get_db)):
    return crud_products.get_products(db)

@router.get("/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_products.get_product_by_id(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud_products.create_product(db, product)

@router.put("/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud_products.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud_products.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}