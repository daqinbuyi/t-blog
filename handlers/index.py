from tornado.web import RequestHandler
from models import post

from markdown import markdown
import config


class IndexHandler(RequestHandler):
    def get(self):
        category_name = self.get_argument("cate", None)
        page = int(self.get_argument("p", 1))
        have_previor = have_next = None
        if page > 1:
            have_previor = page - 1
        if page * config.PAGE_SIZE < post.count_posts(category_name):
            have_next = page + 1
        self.render(
            "index.html",
            posts=post.get_posts(category_name, page),
            markdown=markdown,
            have_previor=have_previor,
            have_next=have_next)
