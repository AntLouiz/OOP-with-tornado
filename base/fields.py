from base.exceptions import ValidationError
from base.models import Model


class ModelType:
    def __init__(self, model):
        if not issubclass(model, Model):
            raise ValueError("Value must be a model class.")
        self.model = model

class BaseField:
    value = None
    def __init__(self, required=False):
        self.required = required

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = self._validate(value)

    def _validate(self, value, *args, **kwargs):
        return value


class StringField(BaseField):
    value = ""

    def __set__(self, obj, value):
        self.value = str(value)

class IntField(BaseField):
    def _validate(self, value):
        if type(value) is not int:
            raise ValidationError("Value isn't an integer.")

        return value


class ChoiceField(BaseField):
    def __init__(self, choices=[], **kwargs):
        self.choices = choices
        super().__init__(**kwargs)

    def __set__(self, obj, value):
        if value not in self.choices:
            raise ValidationError(f'Choice "{value}" not in options.')

        self.value = value


class ListField(BaseField):
    is_model_type = False
    def __init__(self, items=[], **kwargs):
        if type(items) == ModelType:
            self.is_model_type = True

        self.items = items
        super().__init__(**kwargs)

    def __set__(self, obj, values):
        if type(values) is not list:
            raise ValidationError("Value isn't an list.")

        if self.is_model_type:
            for v in values:
                self.items.model(raw_data=v)

        self.value = values


class ForeignField(BaseField):
    def __init__(self, model, **kwargs):
        value_class = self._check_class(model)
        self.value = value_class()
        super().__init__(**kwargs)

    def __set__(self, obj, value):
        if type(value) is list:
            value = filter(self._check_instance, value)

        self.value = self._check_instance(value)

    def _check_class(self, value_cls):
        if not issubclass(value_cls, Model):
            raise ValueError("Value must be an Model subclass.")

        return value_cls

    def _check_instance(self, obj):
        if not isinstance(obj, Model):
            raise ValueError("Value must be an Model instance.")
        return obj


if __name__ == '__main__':
    class Clothes(Model):
        size = IntField()

    class Person(Model):
        age = IntField()
        sex = ChoiceField(choices=['M', 'F', 'O'])
        clothes = ListField(ModelType(Clothes))

    person = Person()
    person.age = 20
    person.sex = 'M'
    person.clothes.size = 38
    print(person.to_primitive())
