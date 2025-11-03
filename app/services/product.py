from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(db: Session) -> List[ProductModel]:
    return db.query(ProductModel).all()


def get_product(db: Session, product_id: int) -> Optional[ProductModel]:
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def create_product(db: Session, data: ProductCreate) -> ProductModel:
    product = ProductModel(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Optional[ProductModel]:
    product = get_product(db, product_id)
    if not product:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> bool:
    product = get_product(db, product_id)
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True


def seed_defaults(db: Session) -> None:
    # seed if empty
    count = db.query(ProductModel).count()
    if count == 0:
        defaults = [
            {"id": 1, "name": "Phone", "description": "", "price": 20000, "quantity": 2},
            {"id": 2, "name": "Laptop", "description": "", "price": 200000, "quantity": 5},
        ]
        for item in defaults:
            db.add(ProductModel(**item))
        db.commit()
