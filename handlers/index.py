from base import BaseHandler

from markdown import markdown


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
            markdown=markdown,
            total=total,
            current_page=page
        )
