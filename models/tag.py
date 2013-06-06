from sqlalchemy import Column, String

from database import db


class Tag(db.Model):
    __tablename__ = "tags"

    name = Column(String(10))

    posts = Column()  # many to many

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Tag:%s>" % self.name
