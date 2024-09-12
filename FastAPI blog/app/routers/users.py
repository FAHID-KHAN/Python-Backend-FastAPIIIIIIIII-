from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(database.get_db)):
    hashed_password = password  # For simplicity, add password hashing later
    new_user = models.User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login():
    return {"message": "User logged in"}


