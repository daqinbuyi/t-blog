from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import db

session = None


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
    session.add(category)
    session.commit()


def get_categories():
    return session.query(Category).order_by(Category.id)


def get_category_by_id(category_id):
    return session.query(Category).get(category_id)


def delete_category_by_id(category_id):
    session.query(Category).filter(Category.id == category_id).delete()


def update(category_id, category_name):
    get_category_by_id(category_id).name = category_name
    session.commit()
