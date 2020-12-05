import tornado.ioloop
import tornado.web
from settings import logger
from urls import urlspatterns


def make_app():
    app = tornado.web.Application(urlspatterns)
    return app


if __name__ == '__main__':
    app = make_app()
    port = 8888
    logger.info(f"Listening to port {port} ...")
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

