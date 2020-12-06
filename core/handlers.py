import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPResponse
from core.gateways import GatewaySelector


class TransactionHandler(tornado.web.RequestHandler):
    gateway_selector = GatewaySelector()

    def post(self, *args, **kwargs):
        print(self.request.body)

        self.write("Hello World")
        return

