
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .import models, crud, schemas, database, auth



app = FastAPI()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


# Token endpoint for user authentication
@app.post("/token")
async def login_for_access_token(form_data: auth.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = auth.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}




# API endpoint to get current user
@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_user)):
    return current_user




# API endpoints for product management
@app.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)




@app.get("/products/", response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)




@app.get("/products/{product_id}", response_model=schemas.Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id=product_id)




# API endpoints for order management
@app.post("/orders/", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.create_order(db=db, order=order, user_id=current_user.id)



@app.get("/orders/", response_model=List[schemas.Order])
async def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.get_orders(db, user_id=current_user.id, skip=skip, limit=limit)



@app.get("/orders/{order_id}", response_model=schemas.Order)
async def read_order(order_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    order = crud.get_order(db, order_id=order_id, user_id=current_user.id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order



# API endpoints for review management
@app.post("/reviews/", response_model=schemas.Review)
async def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.create_review(db=db, review=review, user_id=current_user.id)



@app.get("/reviews/{product_id}", response_model=List[schemas.Review])
async def read_reviews(product_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews(db, product_id=product_id)
