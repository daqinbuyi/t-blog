import tornado.web
from config import site_options


class Article(tornado.web.UIModule):
    def render(self, article, show_all=False):
        return self.render_string(
            "module/article.html",
            article=article,
            show_all=show_all
        )


class Pagination(tornado.web.UIModule):
    def render(self, total, current_page, is_archive=False):
        prev = current_page - 1
        if is_archive:
            page_size = site_options.archive_page_size
        else:
            page_size = site_options.index_page_size
        next = current_page + 1 if page_size * current_page >= total else False
        return self.render_string("module/pagination.html", prev=prev, next=next)


class TagCloud(tornado.web.UIModule):
    def render(self, tags):
        return self.render_string(
            "module/tag_cloud.html",
            tags=tags
        )


class BlogRoll(tornado.web.UIModule):
    def render(self, links):
        return self.render_string(
            "module/blog_roll.html",
            links=links
        )


class RencentPosts(tornado.web.UIModule):
    def render(self, recent_posts):
        return self.render_string(
            "module/recent_posts.html",
            recent_posts=recent_posts
        )


class GoogleAnalytics(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "module/google_analytics.html",
            google_analytics={}
        )
