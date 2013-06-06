
#tornado imports
import tornado.httpserver
import tornado.ioloop

#local imports
import routers
import config


class Application(tornado.web.Application):
    """the application"""
    def __init__(self):
        settings = dict(
            debug=config.DEBUG
        )
        handlers = routers.route
        super(Application, self).__init__(handlers=handlers, **settings)

httpserver = tornado.httpserver.HTTPServer(Application())
httpserver.listen(8888)

tornado.ioloop.IOLoop.instance().start()
