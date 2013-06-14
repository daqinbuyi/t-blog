from tornado.web import RequestHandler
from models import category


class IndexHandler(RequestHandler):
    def get(self):
        self.render("category.html", categories=category.get_categories() )

    def post(self):
        category.add(category.Category(self.get_argument("name")))
        self.redirect("/admin/categories")
