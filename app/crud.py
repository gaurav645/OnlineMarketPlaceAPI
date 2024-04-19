
from sqlalchemy.orm import Session
from . import models, schemas
from . import auth


# User CRUD operations

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Product CRUD operations

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Order CRUD operations

def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(**order.dict(), user_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Order).filter(models.Order.user_id == user_id).offset(skip).limit(limit).all()

def get_order(db: Session, order_id: int, user_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id, models.Order.user_id == user_id).first()

# Review CRUD operations

def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, product_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.product_id == product_id).offset(skip).limit(limit).all()
