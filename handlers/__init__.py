import tornado.web
from database import db
from config import site_options
from model import Post, Category, Tag
from sqlalchemy import func


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = db.Session()

    def get_current_user(self):
        return self.get_secure_cookie("status")

    def render(self, template_name, **kwargs):
        if not self.request.path.startswith("/admin"):
            kwargs["tags"] = self.get_tags()
            kwargs["recent_posts"] = self.get_recent_posts()
            kwargs["links"] = [dict(name="test", url="#"), ]
        super(BaseHandler, self).render(
            template_name,
            site_options=site_options,
            **kwargs
        )

    def on_finish(self):
        self.db.close()

    def count_posts(self, category_name=None):
        my_query = self.db.query(Post).join(Post.category)
        if category_name:
            my_query = my_query.filter(Category.name == category_name)
        return my_query.count()

    def get_posts(self, category_name=None, page=1):
        my_query = self.db.query(Post).join(Post.category)
        if category_name:
            my_query = my_query.filter(Category.name == category_name)
        result = my_query.\
            order_by(Post.id.desc())[(page-1)*site_options["index_page_size"]:page*site_options["index_page_size"]]
        return result

    def get_recent_posts(self):
        return self.db.query(Post.id, Post.title).order_by(Post.post_time.desc())[:5]

    def get_headers(self, category_id=None):
        my_query = self.db.query(Post.id, Post.title, Category.name, Post.post_time).join(Post.category)
        if category_id:
            my_query = my_query.filter(Post.category_id == category_id)
        return my_query.order_by(Post.id.desc()).all()
