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


class EditHandler(RequestHandler):
    def get(self, tag_id):
        self.render("tag_edit.html", tag=tag.get_tag_by_id(int(tag_id)))

    def post(self, tag_id):
        tag.update(int(tag_id), self.get_argument("name").strip())
        self.redirect("/admin/tags")
