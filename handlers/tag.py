from tornado.web import authenticated
from . import BaseHandler


class IndexHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("tag.html", tags=self.get_tags())

    @authenticated
    def post(self):
        tag_name = self.get_argument("name")
        print tag_name
        self.add_tag(self.Tag(tag_name))
        self.redirect("/admin/tags")


class EditHandler(BaseHandler):
    @authenticated
    def get(self, tag_id):
        self.render("tag_edit.html", tag=self.get_tag_by_id(int(tag_id)))

    @authenticated
    def post(self, tag_id):
        self.update_tag(int(tag_id), self.get_argument("name").strip())
        self.redirect("/admin/tags")
