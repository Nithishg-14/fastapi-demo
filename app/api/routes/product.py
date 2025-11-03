from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services.product import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/api/v2", tags=["Product"])


@router.get("/products", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return get_products(db)


@router.get("/product/{id}", response_model=ProductOut)
def retrieve_product(id: int, db: Session = Depends(get_db)):
    product = get_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/product", response_model=ProductOut, status_code=201)
def create_product_endpoint(payload: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, payload)


@router.put("/product/{id}", response_model=ProductOut)
def update_product_endpoint(id: int, payload: ProductUpdate, db: Session = Depends(get_db)):
    product = update_product(db, id, payload)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/product/{id}", status_code=204)
def delete_product_endpoint(id: int, db: Session = Depends(get_db)):
    ok = delete_product(db, id)
    if not ok:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
