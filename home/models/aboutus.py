from django.db.models import Model, CharField, TextField


class AboutUs(Model):
    title = CharField(max_length=100)
    subtitle = CharField(max_length=100)
    description = TextField()
    description2 = TextField()

    def __str__(self):
        return self.title
