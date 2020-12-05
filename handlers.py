import tornado.ioloop
import tornado.web
from gateways import GatewaySelector
from tornado.httpclient import HTTPResponse


class TransactionHandler(tornado.web.RequestHandler):
    gateway_selector = GatewaySelector()

    def post(self, *args, **kwargs):
        print(self.request.body)

        self.write("Hello World")
        return

