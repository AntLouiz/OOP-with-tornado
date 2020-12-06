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
        keys_to_ignore = ['__module__', '__doc__']
        d = dict(cls.__dict__)
        for key in keys_to_ignore:
            d.pop(key)
        primitive = {key: d[key].value for key in d}

        return primitive


class Customer(Model):
    private_key = StringField()
    public_key = StringField()
    name = StringField()
    cnpj = StringField()
    gateways = ListField()
