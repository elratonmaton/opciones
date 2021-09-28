from django.db.models import Model, CharField, ImageField, TextField


class ContactPage(Model):
    name = CharField(max_length=100)
    map_latitude = CharField(max_length=20)
    map_longitude = CharField(max_length=20)
    map_pin_title = CharField(max_length=20)

    def __str__(self):
        return self.name
