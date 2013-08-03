
#sqlalchemy imports
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator, Text

#local imports
from database import db
from markdown import markdown

post_tags = Table(
    "post_tag_map",
    db.Model.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")))


class MarkdownText(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is not None and isinstance(value, str):
            return value
        return None

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return markdown(value)


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    title = Column(String(50), nullable=False)
    en_title = Column(String(50), nullable=False)
    content = Column(MarkdownText, nullable=False)
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


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    posts = relationship("Post", order_by="Post.id")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category: %s>" % self.name


class Tag(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    posts = relationship("Post", secondary=post_tags)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Tag:%s>" % self.name
