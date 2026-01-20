from fastapi import FastAPI

from routers import articles, comments
from database import SessionLocal, engine, get_db, Base
from models.article import Article
from models.comment import Comment

from routers import articles

# Create tables
Base.metadata.create_all(bind=engine)

# Example: Create sample data
with SessionLocal() as session:
    article_length = session.query(Article).count()
    article = Article(title=f"Sample Article {article_length + 1}")

    comments_of_article = len(article.comments)
    comment1 = Comment(content=f"This is comment {comments_of_article + 1}.")
    comment2 = Comment(content=f"This is comment {comments_of_article + 2}.")

    article.comments = [comment1, comment2]
    session.add(article)
    session.commit()

# Query and print first article with comments
with SessionLocal() as session:
    first_article = articles.get_articles(db=session)[0]
    print(f"Article ID: {first_article.id}, Title: {first_article.title}")
    for comment in first_article.comments:
        print(f" - Comment ID: {comment.id}, Content: {comment.content}")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

app.include_router(articles.router, prefix="/articles", tags=["articles"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])