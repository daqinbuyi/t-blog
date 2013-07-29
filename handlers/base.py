import tornado.web
from database import db
from models import post, category, tag
from config import site_options


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = db.Session()
        self.postservice = post
        self.categoryservice = category
        self.tagservice = tag
        self.postservice.session = self.categoryservice.session = self.tagservice.session = self.session

    def get_current_user(self):
        return self.get_secure_cookie("status")

    def render(self, template_name, **kwargs):
        if not self.request.path.startswith("/admin"):
            kwargs["tags"] = self.tagservice.get_tags()
            kwargs["recent_posts"] = self.postservice.get_recent_posts()
            kwargs["links"] = [dict(name="test", url="#"), ]
        super(BaseHandler, self).render(
            template_name,
            site_options=site_options,
            **kwargs
        )

    def on_finish(self):
        self.session.close()
