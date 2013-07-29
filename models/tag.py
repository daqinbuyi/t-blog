from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import db
from models.association import post_tags

session = None


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
    session.add(tag)
    session.commit()


def get_tags():
    return session.query(Tag)


def get_tag_by_id(tag_id):
    return session.query(Tag).get(tag_id)


def get_tags_by_ids(ids):
    ids = [int(i) for i in ids]
    return session.query(Tag).filter(Tag.id.in_(ids)).all()


def update(tag_id, tag_name):
    get_tag_by_id(tag_id).name = tag_name
    session.commit()
