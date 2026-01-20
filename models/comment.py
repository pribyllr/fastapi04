from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from pydantic import BaseModel

from models.base import Base

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    
    article = relationship("Article", back_populates="comments")

class CommentRead(BaseModel):
    id: int
    content: str
    article_id: int