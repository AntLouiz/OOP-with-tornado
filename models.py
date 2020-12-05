from fields import (
    StringField,
    ListField
)


class Model:
    def __getitem__(self, key):
        value = getattr(self, key)
        return value

    @classmethod
    def to_primitive(cls):
        d = dict(cls.__dict__)
        d.pop('__module__')
        d.pop('__doc__')
        primitive = {key: d[key].value for key in d}

        return primitive


class Customer(Model):
    private_key = StringField()
    public_key = StringField()
    name = StringField()
    cnpj = StringField()
    gateways = ListField()
