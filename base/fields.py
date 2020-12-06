from base.exceptions import ValidationError
from base.models import Model


class BaseField:
    value = None
    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = self._validate(value)

    def _validate(self, value, *args, **kwargs):
        return value


class StringField(BaseField):
    pass


class IntField(BaseField):
    def _validate(self, value):
        if type(value) is not int:
            raise ValidationError("Value isn't an integer.")

        return value


class ChoiceField(BaseField):
    def __init__(self, choices=[]):
        self.choices = choices

    def __set__(self, obj, value):
        if value not in self.choices:
            raise ValidationError(f'Choice "{value}" not in options.')

        self.value = value


class ListField(BaseField):
    def __init__(self, items=[]):
        self.items = items

    def __set__(self, obj, value):
        if type(value) is not list:
            raise ValidationError("Value isn't an list.")

        self.value = value


class ForeignField(BaseField):
    def __init__(self, model):
        value_class = self._check_class(model)
        self.value = value_class()

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
        clothes = ForeignField(Clothes)

    person = Person()
    person.age = 20
    person.sex = 'M'
    person.clothes.size = 38
    print(person.to_primitive())
