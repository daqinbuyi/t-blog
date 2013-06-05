from sqlalchemy import Column, Integer, String

from database import db

class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Post:%s>" % self.name

def get_posts():
        return db.session.query(Post).all()

def save(post):
        db.session.add(post)
