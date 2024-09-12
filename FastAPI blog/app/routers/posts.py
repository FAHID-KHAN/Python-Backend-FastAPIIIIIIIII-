from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_post(title: str, content: str, db: Session = Depends(database.get_db)):
    new_post = models.Post(title=title, content=content)
    db.add(new_post)
    db.commit()
    return {"message": "Post created"}

@router.get("/")
def get_posts(db: Session = Depends(database.get_db)):
    return db.query(models.Post).all()

