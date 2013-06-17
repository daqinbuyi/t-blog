
#sqlalchemy imports
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, joinedload

#local imports
from database import db
from models.association import post_tags
from models.category import Category


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    title = Column(String(30), nullable=False)
    content = Column(Text, nullable=False)
    post_time = Column(DateTime, nullable=False)

    #many to many Post<->Tag
    tags = relationship("Tag", secondary=post_tags)

    #many to one Post<->Category
    category = relationship("Category")

    def __init__(self, title=None, content=None, post_time=None):
        self.title = title
        self.content = content
        self.post_time = post_time

    def __repr__(self):
        return "<Post:%s>" % self.title


#methods to do with Post
def get_posts():
    return db.session.query(Post).options(joinedload(Post.category)).all()


def get_headers():
    return db.session.query(Post.id, Post.title, Category.name, Post.post_time).filter(Category.id == Post.category_id).all()


def get_post_by_id(post_id):
    return db.session.query(Post).get(post_id)


def add(post):
    db.session.add(post)
    db.session.commit()


def count():
    db.session.query(Post).count()


def update():
    db.session.commit()
