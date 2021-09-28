from django.db.models import Model, CharField, ImageField, TextField


class SocialResponsability(Model):
    title = CharField(max_length=100)
    block_1_image = ImageField(upload_to='home/social')
    block_1_description_title = TextField()
    block_1_description = TextField()

    block_2_image = ImageField(upload_to='home/social')
    block_2_description_title = TextField()

    def __str__(self):
        return self.title
