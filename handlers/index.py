from tornado.web import RequestHandler
from models import post

class IndexHandler(RequestHandler):
    def get(self):
        for article in post.get_posts():
            self.write(article.name)