
#sqlalchemy imports
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, joinedload

#local imports
from database import db
from models.association import post_tags


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

    def __init__(self, title, content, post_time):
        self.title = title
        self.content = content
        self.post_time = post_time

    def __repr__(self):
        return "<Post:%s>" % self.title


#methods to do with Post
def get_posts():
    return db.session.query(Post).options(joinedload(Post.category)).all()


def add(post):
    db.session.add(post)


def count():
    db.session.query(Post).count()
