from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import db


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    posts = relationship("Post", order_by="Post.id")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category: %s>" % self.name


def add(category):
    db.session.add(category)
    db.session.commit()


def get_categories():
    return db.session.query(Category).order_by(Category.id)


def get_category_by_id(category_id):
    return db.session.query(Category).filter(Category.id == category_id).one()
