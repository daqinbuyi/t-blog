from sqlalchemy import Column, Integer, String, DateTime

from database import db


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    content = Column(String)
    post_time = Column(DateTime)

    tags = Column()  # many to many

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Post:%s>" % self.name


#methods to do with Post
def get_posts():
    return db.session.query(Post).all()


def save(post):
    db.session.add(post)
