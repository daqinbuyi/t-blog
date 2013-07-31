from . import BaseHandler
from tornado.web import authenticated
from handlermixin import CategoryMixin


class IndexHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("category.html", categories=self.get_categories())

    @authenticated
    def post(self):
        self.add_category(self.Category(self.get_argument("name")))
        self.redirect("/admin/categories")


class EditHandler(BaseHandler):
    @authenticated
    def get(self, category_id):
        self.render("category_edit.html", category=self.get_category_by_id(int(category_id)))

    @authenticated
    def post(self, category_id):
        self.update_category(category_id, self.get_argument("name"))
        self.redirect("/admin/categories")


class DeleteHandler(BaseHandler):
    @authenticated
    def get(self, id):
        self.render("category_delete.html", category=self.get_category_by_id(int(id)))

    @authenticated
    def delete(self):
        self.delete_by_id(int(self.get_argument("id")))
        self.redirect("/admin/categories")
