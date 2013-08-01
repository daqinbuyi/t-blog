import tornado.web
from database import db
from config import site_options
from mixin import BaseMixin


class BaseHandler(tornado.web.RequestHandler, BaseMixin):
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

    def _get_limit_offset(self, page):
        offset = (page - 1) * site_options["index_page_size"]
        limit = site_options["index_page_size"]
        return limit, offset
