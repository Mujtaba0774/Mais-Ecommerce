from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/process", response_model=schemas.Payment)
def process_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return crud.process_payment(db=db, payment=payment)
