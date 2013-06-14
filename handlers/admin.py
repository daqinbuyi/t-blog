from tornado.web import RequestHandler
from models import post


class IndexHandler(RequestHandler):
    def get(self):
        self.render("admin.html")
