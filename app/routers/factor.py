from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import factor as crud_factor
from app.schemas.factor import FactorCreate, FactorOut

router = APIRouter(
    prefix="/factors",
    tags=["Factors"]
)

@router.get("/", response_model=list[FactorOut])
def read_factors(db: Session = Depends(get_db)):
    return crud_factor.get_factors(db)

@router.get("/{factor_id}", response_model=FactorOut)
def read_factor(factor_id: int, db: Session = Depends(get_db)):
    factor = crud_factor.get_factor_by_id(db, factor_id)
    if not factor:
        raise HTTPException(status_code=404, detail="Factor not found")
    return factor

@router.post("/", response_model=FactorOut)
def create_factor(factor: FactorCreate, db: Session = Depends(get_db)):
    return crud_factor.create_factor(db, factor)

@router.delete("/{factor_id}")
def delete_factor(factor_id: int, db: Session = Depends(get_db)):
    deleted = crud_factor.delete_factor(db, factor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Factor not found")
    return {"detail": "Factor deleted successfully"}