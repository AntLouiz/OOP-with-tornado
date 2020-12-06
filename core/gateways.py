from base.fields import (
    StringField,
    IntField,
    ChoiceField,
)
from base.exceptions import ValidationError


class BaseGateway:
    def __init__(self, merchant_key, subordinate_key,
                 api_key, soft_descriptor, is_sandbox=True,
                 *args, **kwargs):
        self.merchant_key = merchant_key
        self.subordinate_key = subordinate_key
        self.api_key = api_key
        self.soft_descriptor = soft_descriptor
        self.is_sandbox = is_sandbox

    def authorize(self, *args, **kwargs):
        raise NotImplementedError

    def capture(self, *args, **kwargs):
        raise NotImplementedError

    def refund(self, *args, **kwargs):
        raise NotImplementedError


class GatewayResponse:
    gateway = StringField()
    amount = IntField()
    status = ChoiceField(choices=['0', '1', '2'])
    return_code = ChoiceField(choices=['10', '11'])
    reason = StringField()

    def __init__(self, *args, **kwargs):
        for key in kwargs:
            attr = getattr(self, key)
            value = kwargs[key]
            setattr(self, key, value)


class GatewayFactory:
    gateways_options = {}

    @classmethod
    def register(cls, gateway_type):
        def inner_func(subclass):
            cls.gateways_options[gateway_type] = subclass
            return subclass
        return inner_func

    @classmethod
    def create(cls, gateway_type=None):
        gateway = cls.gateways_options.get(gateway_type)
        if not gateway:
            raise ValueError("Gateway not found.")

        return gateway

    @property
    def gateways(self):
        keys = [key for key in self.gateways_options]
        return keys


@GatewayFactory.register('braspag')
class BraspagGateway(BaseGateway):
    pass

@GatewayFactory.register('ingenico')
class IngenicoGateway(BaseGateway):
    pass


if __name__ == '__main__':
    r = GatewayResponse(amount=1, status='0')
    print(r.amount)
    print(r.status)

    r.amount = 22
    print(r.amount)
    print(r.status)
