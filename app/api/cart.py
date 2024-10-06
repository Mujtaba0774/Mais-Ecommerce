from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.CartItem)
def add_to_cart(cart_item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    return crud.add_item_to_cart(db=db, cart_item=cart_item)

@router.get("/", response_model=List[schemas.CartItem])
def get_cart(db: Session = Depends(get_db)):
    return crud.get_cart(db=db)
