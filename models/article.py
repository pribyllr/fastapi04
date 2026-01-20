from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import List
from models.comment import CommentRead
from models.base import Base

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    comments = relationship("Comment", back_populates="article")

class ArticleRead(BaseModel):
    id: int
    title: str
    comments: List[CommentRead] = []
