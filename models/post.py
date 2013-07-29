
#sqlalchemy imports
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship

#local imports
from database import db
from models.association import post_tags
from models.category import Category
from config import site_options

session = None


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


def count_posts(category_name=None):
    my_query = session.query(Post).join(Post.category)
    if category_name:
        my_query = my_query.filter(Category.name == category_name)
    return my_query.count()


def get_posts(category_name=None, page=1):
    my_query = session.query(Post).join(Post.category)
    if category_name:
        my_query = my_query.filter(Category.name == category_name)
    result = my_query.order_by(Post.id.desc())[(page-1)*site_options["page_size"]:page*site_options["page_size"]]
    return result


def get_recent_posts():
    return session.query(Post.id, Post.title).order_by(Post.post_time.desc())[:5]


def get_headers(category_id=None):
    my_query = session.query(Post.id, Post.title, Category.name, Post.post_time).join(Post.category)
    if category_id:
        my_query = my_query.filter(Post.category_id == category_id)
    return my_query.order_by(Post.id.desc()).all()


def get_header_by_id(post_id):
    return session.query(Post.id, Post.title).filter(Post.id == post_id).one()


def get_post_by_id(post_id):
    return session.query(Post).get(post_id)


def add(post):
    session.add(post)
    session.commit()


def count():
    session.query(Post).count()


def update():
    session.commit()


def delete_post_by_id(post_id):
    session.query(Post).filter(Post.id == post_id).delete()


def get_category_info():
    return session.query(Category.name, func.count(Post.id)).join(Post.category).group_by(Post.category_id).all()
