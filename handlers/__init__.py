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

    def get_header_by_id(self, post_id):
        return self.db.query(Post.id, Post.title).filter(Post.id == post_id).one()

    def get_post_by_id(self, post_id):
        return self.db.query(Post).get(post_id)

    def add_post(self, post):
        self.db.add(post)
        self.db.commit()

    def count(self):
        self.db.query(Post).count()

    def update_post(self):
        self.db.commit()

    def delete_post_by_id(self, post_id):
        self.db.query(Post).filter(Post.id == post_id).delete()

    def get_category_info(self):
        return self.db.query(Category.name, func.count(Post.id)).join(Post.category).group_by(Post.category_id).all()

    def add_category(self, category):
        self.db.add(category)
        self.db.commit()

    def get_categories(self):
        return self.db.query(Category).order_by(Category.id)

    def get_category_by_id(self, category_id):
        return self.db.query(Category).get(category_id)

    def delete_category_by_id(self, category_id):
        self.db.query(Category).filter(Category.id == category_id).delete()

    def update_category(self, category_id, category_name):
        self.get_category_by_id(category_id).name = category_name
        self.db.commit()

    def add_tag(self, tag):
        self.db.add(tag)
        self.db.commit()

    def get_tags(self):
        return self.db.query(Tag)

    def get_tag_by_id(self, tag_id):
        return self.db.query(Tag).get(tag_id)

    def get_tags_by_ids(self, ids):
        ids = [int(i) for i in ids]
        return self.db.query(Tag).filter(Tag.id.in_(ids)).all()

    def update_tag(self, tag_id, tag_name):
        self.get_tag_by_id(tag_id).name = tag_name
        self.db.commit()
