import tornado.web
from tornado.web import authenticated
from . import BaseHandler
from handlermixin import PostMixin, TagMixin, CategoryMixin

from datetime import datetime


class AddHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render(
            "post_add.html",
            tags=self.get_tags(),
            categories=self.get_categories()
        )

    @authenticated
    def post(self):
        my_post = self.Post()
        my_post.title = self.get_argument("title")
        my_post.content = self.get_argument("content")
        my_post.category_id = int(self.get_argument("category"))
        for tag_item in self.get_tags_by_ids(self.get_arguments("tags")):
            my_post.tags.append(tag_item)
        my_post.post_time = datetime.now()
        self.add_post(my_post)
        self.redirect("/admin/posts")


class ListHandler(BaseHandler):
    @authenticated
    def get(self):
        category_id = self.get_argument("cate", None)
        if category_id:
            category_id = int(category_id)
        self.render("post_list.html", headers=self.get_headers(category_id))


class ShowHandler(BaseHandler):
    def get(self, id):
        my_post = self.get_post_by_id(int(id))
        if my_post:
            self.render("post.html", post=my_post)
        else:
            raise tornado.web.HTTPError(404)


class EditHandler(BaseHandler):
    @authenticated
    def get(self, id):
        my_post = self.get_post_by_id(int(id))
        selected_tags = [i.id for i in my_post.tags]
        self.render(
            "post_edit.html",
            post=my_post,
            tags=self.get_tags(),
            selected_tags=selected_tags,
            categories=self.get_categories()
        )

    @authenticated
    def post(self, post_id):
        my_post = self.get_post_by_id(post_id)
        my_post.title = self.get_argument("title")
        my_post.content = self.get_argument("content")
        my_post.category_id = int(self.get_argument("category"))
        my_post.tags = []
        for tag_item in self.get_tags_by_ids(self.get_arguments("tags")):
            my_post.tags.append(tag_item)
        self.update_post()
        self.redirect("/admin/posts")


class DeleteHandler(BaseHandler):
    @authenticated
    def get(self, post_id):
        self.render("post_delete.html", post=self.get_header_by_id(int(post_id)))

    @authenticated
    def post(self, post_id):
        self.delete_post_by_id(int(post_id))
        self.redirect("/admin/posts")
