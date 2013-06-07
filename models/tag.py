from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import db
from models.association import post_tags


class Tag(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    posts = relationship("Post", secondary=post_tags)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Tag:%s>" % self.name


def add(tag):
    db.session.add(tag)
