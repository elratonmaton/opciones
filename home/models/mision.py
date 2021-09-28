from django.db.models import Model, CharField, TextField, ImageField


class Mision(Model):
    image = ImageField(upload_to='home/mission')
    description = TextField()
    description2 = TextField()
    signature = ImageField(upload_to='home/mission')

    def __str__(self):
        return self.description
