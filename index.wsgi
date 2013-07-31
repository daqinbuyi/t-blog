
#tornado imports
import tornado.wsgi

#local imports
import routers
import config
import uimodules
import os

settings = dict(
    debug=config.DEBUG,
    template_path=os.path.join(os.path.dirname(__file__), "themes/modernist"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    login_url="/admin/login",
    cookie_secret=config.COOKIE_SECRET,
    ui_modules=uimodules
)


class WSGIApplication(tornado.wsgi.WSGIApplication):
    """the main application"""
    def __init__(self):
        super(WSGIApplication, self).__init__(handlers=routers.route, **settings)


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers=routers.route, **settings)


if "SERVER_SOFTWARE" in os.environ:
    import sae
    application = sae.create_wsgi_app(WSGIApplication())
else:
    import tornado.httpserver
    httpserver = tornado.httpserver.HTTPServer(Application())
    httpserver.listen(8888, address="0.0.0.0")

    tornado.ioloop.IOLoop.instance().start()
