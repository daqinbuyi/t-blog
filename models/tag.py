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
    db.session.commit()


def get_tags():
    return db.session.query(Tag)


def get_tag_by_id(tag_id):
    return db.session.query(Tag).filter(Tag.id == tag_id).one()


def get_tags_by_ids(ids):
    ids = [int(i) for i in ids]
    return db.session.query(Tag).filter(Tag.id.in_(ids)).all()
