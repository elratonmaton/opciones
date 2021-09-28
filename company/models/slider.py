from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE


class Slider(Model):
    image = ImageField(upload_to='company/sliders')
    title = CharField(max_length=100)
    subtitle = CharField(max_length=100)
    company = ForeignKey('company.Company', on_delete=CASCADE)

    def __str__(self):
        return self.title
