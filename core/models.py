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
    private_key = StringField()
    public_key = StringField()
    name = StringField()
    cnpj = StringField()
    gateways = ForeignField(Gateway)

    class Meta:
        collection = database.customers