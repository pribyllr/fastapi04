from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.comment import Comment, CommentRead

router = APIRouter()

@router.get("/articles/{article_id}/comments", response_model=List[CommentRead])
def get_comments_by_article_id(article_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.article_id == article_id).all()
    if comments is None:
        raise HTTPException(status_code=404, detail="Comments not found for the given article")
    return comments