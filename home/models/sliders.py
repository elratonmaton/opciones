from django.db.models import Model, CharField, ImageField


class Slider(Model):
    image = ImageField(upload_to='home/sliders')
    title = CharField(max_length=100)
    subtitle = CharField(max_length=100)

    def __str__(self):
        return self.title
