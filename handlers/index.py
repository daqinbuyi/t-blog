from base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        category = self.get_argument("cate", None)
        tag = self.get_argument("tag", None)
        page = int(self.get_argument("p", 1))
        total = self.postservice.count_posts(category)
        self.render(
            "index.html",
            category=category,
            tag=tag,
            articles=self.postservice.get_posts(category, page),
            total=total,
            current_page=page
        )


class ArchiveHandler(BaseHandler):
    def get(self):
        page = int(self.get_argument("p", 1))
        total = self.postservice.count_posts()
        self.render(
            "archive.html",
            articles=self.postservice.get_headers(),
            current_page=page,
            total=total
        )
