import json
import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPResponse
from core.models import Customer, Gateway
from base.exceptions import ValidationError, DataError


class CustomerHandler(tornado.web.RequestHandler):
    async def post(self, *args, **kwargs):
        body = self.request.body
        body_decoded = json.loads(body)

        try:
            post_data = Customer(raw_data=body_decoded)
        except (ValueError, ValidationError, AssertionError, DataError) as e:
            self.set_status(400)
            self.write({'error': str(e)})
            return

        cnpj = post_data.cnpj
        exists_customer = await Customer.objects().find(cnpj=cnpj)
        if exists_customer:
            self.set_status(400)
            self.write({'error': 'Customer already exists'})
            return

        data = post_data.to_primitive()
        result = await Customer.objects().create(data)

        response_data = data
        response_data.update({"_id": str(result.inserted_id)})

        self.set_status(201)
        self.write(response_data)
        return
