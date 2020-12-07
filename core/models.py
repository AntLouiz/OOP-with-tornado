from base.models import Model
from base.fields import (
    StringField,
    ListField,
    ForeignField,
    ModelType,
)
from settings import database

class Gateway(Model):
    slug = StringField(required=True)
    merchant_id = StringField(required=True)
    subordinate_id = StringField()
    api_key = StringField(required=True)

    class Meta:
        collection = database.gateways


class Customer(Model):
    private_key = StringField(required=True)
    public_key = StringField(required=True)
    name = StringField(required=True)
    cnpj = StringField(required=True)
    gateways = ListField(ModelType(Gateway))

    class Meta:
        collection = database.customers