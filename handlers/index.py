from tornado.web import RequestHandler
from models import post

from markdown import markdown


class IndexHandler(RequestHandler):
    def get(self):
        self.render(
            "index.html",
            posts=post.get_posts(),
            markdown=markdown,
            have_previor=False,
            have_next=False)
