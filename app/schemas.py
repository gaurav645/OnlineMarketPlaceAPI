
from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    category: str
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    user_id: int
    product_id: int
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True
