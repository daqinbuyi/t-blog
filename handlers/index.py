from tornado.web import RequestHandler
from models import post


class IndexHandler(RequestHandler):
    def get(self):
        print "hah"
        posts = post.get_posts()
        for item in posts:
            print item.title
            print item.category.name
        # for article in posts:
        #     self.write(article.title)
        #     self.write(article.tags[0].tag.name)
