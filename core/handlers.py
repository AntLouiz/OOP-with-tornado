import json
import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPResponse
from core.models import Customer


class CustomerHandler(tornado.web.RequestHandler):
    async def post(self, *args, **kwargs):
        body = self.request.body
        body_decoded = json.loads(body)

        try:
            post_data = Customer(raw_data=body_decoded)
        except ValueError:
            self.set_status(400)
            self.write({'error': 'Invalid data.'})
            return

        exists_customer = await Customer.objects().find(body_decoded)
        self.write(body_decoded)
        return
