from django.db.models import Model, CharField


class Autor(Model):
    names = CharField(max_length=100)
    last_names = CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.names, self.last_names)
