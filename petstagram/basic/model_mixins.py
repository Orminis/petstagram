class StrFromFieldsMixin:
    """
    Mixin in which `str_fields` tuple is given in the child class and overrides __str__ method.
    Class Meta is used when we want to use Django specific methods, but this is pure python.
    """
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f"{name} = {value}" for (name, value) in fields)
