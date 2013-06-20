from tornado.web import authenticated
from base import BaseHandler
from models import tag


class IndexHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("tag.html", tags=tag.get_tags())

    @authenticated
    def post(self):
        tag_name = self.get_argument("name")
        print tag_name
        tag.add(tag.Tag(tag_name))
        self.redirect("/admin/tags")


class EditHandler(BaseHandler):
    @authenticated
    def get(self, tag_id):
        self.render("tag_edit.html", tag=tag.get_tag_by_id(int(tag_id)))

    @authenticated
    def post(self, tag_id):
        tag.update(int(tag_id), self.get_argument("name").strip())
        self.redirect("/admin/tags")
