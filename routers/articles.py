from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.article import Article, ArticleRead
from models.comment import Comment
from typing import List

router = APIRouter()

@router.get("/", response_model=List[ArticleRead])
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    if not articles:
        print("No articles found")
    return articles

@router.get("/{article_id}", response_model=ArticleRead)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article