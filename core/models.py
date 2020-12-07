from base.models import Model
from base.fields import (
    StringField,
    ListField,
    ForeignField
)
from settings import database

class Gateway(Model):
    slug = StringField()
    merchant_id = StringField()
    subordinate_id = StringField()
    api_key = StringField()

    class Meta:
        collection = database.gateways


class Customer(Model):
    private_key = StringField(required=True)
    public_key = StringField(required=True)
    name = StringField(required=True)
    cnpj = StringField(required=True)
    gateways = ListField()

    class Meta:
        collection = database.customers