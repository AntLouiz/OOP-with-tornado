import tornado.ioloop
import tornado.web
import motor
from settings import logger, database
from core.urls import urlspatterns


def make_app():
    settings = {
        "database": database
    }
    app = tornado.web.Application(urlspatterns, settings=settings)
    return app


if __name__ == '__main__':
    app = make_app()
    port = 8888
    logger.info(f"Listening to port {port} ...")
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

