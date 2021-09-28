from django.db.models import Model, CharField, TextField


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name
