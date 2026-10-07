from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product import ProductCreate

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        code=product.code,
        price=product.price,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product_by_id(db, product_id)
    if db_product:
        db_product.name = product.name
        db_product.code = product.code
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False