from exceptions import ValidationError


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


if __name__ == '__main__':
    class Person:
        age = IntField()
        sex = ChoiceField(choices=['M', 'F', 'O'])

    person = Person()
    person.age = 20
    person.sex = 'M'
    print(person.age)
    print(person.sex)
