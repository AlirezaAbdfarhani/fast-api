from sqlalchemy.orm import Session
from app.models.factor_model import Factor
from app.models.factor_details_model import FactorItem
from app.models.product_model import Product
from app.schemas.factor import FactorCreate
from fastapi import HTTPException


def get_factors(db: Session):
    return db.query(Factor).all()


def get_factor_by_id(db: Session, factor_id: int):
    return db.query(Factor).filter(Factor.id == factor_id).first()


def create_factor(db: Session, factor: FactorCreate):
    db_factor = Factor(cid=factor.customer_id, total=0)
    db.add(db_factor)
    db.flush()

    total_sum = 0
    for item in factor.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            db.rollback()
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found",
            )

        item_sum = item.no * product.price
        db_item = FactorItem(
            factor_id=db_factor.id,
            product_id=item.product_id,
            no=item.no,
            fee=int(product.price),
            sum_fee=int(item_sum),
        )
        db.add(db_item)
        total_sum += item_sum

    db_factor.total = int(total_sum)
    db.commit()
    db.refresh(db_factor)
    return db_factor


def delete_factor(db: Session, factor_id: int):
    db_factor = get_factor_by_id(db, factor_id)
    if db_factor:
        db.delete(db_factor)
        db.commit()
        return True
    return False