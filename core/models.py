from base.models import Model
from base.fields import (
    StringField,
    ListField
)


class Gateway(Model):
    slug = StringField()
    merchant_id = StringField()
    subordinate_id = StringField()
    api_key = StringField()


class Customer(Model):
    private_key = StringField()
    public_key = StringField()
    name = StringField()
    cnpj = StringField()
    gateways = ForeignField(Gateway)
