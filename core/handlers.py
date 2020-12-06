import json
import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPResponse
from core.gateways import GatewayFactory


class TransactionHandler(tornado.web.RequestHandler):
    gateway_factory = GatewayFactory()

    def post(self, *args, **kwargs):
        body = self.request.body
        body_decoded = json.loads(body)

        self.write(body_decoded)
        return

