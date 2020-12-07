from base.managers import CollectionManager


class Model:
    def __init__(self, raw_data={}):
        if not raw_data:
            return

        requireds = self._required_fields()
        for key in raw_data:
            assert hasattr(self, key), f'Rogue field "{key}".'
            value = raw_data[key]
            try:
                requireds.remove(key)
            except ValueError:
                pass 

            setattr(self, key, value)
        if requireds:
            raise ValueError(f"Missing required field(s): {requireds}")

    def __getitem__(self, key):
        value = getattr(self, key)
        return value

    @classmethod
    def to_primitive(cls):
        d = dict(cls.__dict__)
        primitive = {}
        for key in d:
            if cls._filter_key(key):
                continue

            field_instance = d[key]
            try:
                value = field_instance.value
                if type(value) is list:
                    value = [v.to_primitive() for v in value]
                else:
                    value = value.to_primitive()
                primitive[key] = value
            except AttributeError:
                primitive[key] = field_instance.value

        return primitive

    def _required_fields(self):
        attrs = []
        all_attrs = type(self).__dict__
        for key in all_attrs:
            attr_instance = all_attrs[key]
            if self._filter_key(key) or not attr_instance.required:
                continue
            attrs.append(key)
        return attrs

    @classmethod
    def _filter_key(cls, key):
        keys_to_ignore = [ '__main__', '__module__', '__doc__', 'Meta']
        return key in keys_to_ignore

    @classmethod
    def objects(self, *args, **kwargs):
        return CollectionManager(self.Meta().collection) 

    class Meta:
        collection = None
