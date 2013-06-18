from tornado.web import RequestHandler
from models import post


class IndexHandler(RequestHandler):
    def get(self):
        print self.request
        self.render("admin.html")
