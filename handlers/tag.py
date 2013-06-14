from tornado.web import RequestHandler
from models import tag


class IndexHandler(RequestHandler):
    def get(self):
        self.render("tag.html", tags=tag.get_tags())

    def post(self):
        tag_name = self.get_argument("name")
        print tag_name
        tag.add(tag.Tag(tag_name))
        self.redirect("/admin/tags")
