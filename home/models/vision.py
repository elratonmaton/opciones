from django.db.models import Model, CharField, TextField, ImageField


class Vision(Model):
    image = ImageField(upload_to='home/vision')
    description = TextField()
    description2 = TextField()

    def __str__(self):
        return self.description
