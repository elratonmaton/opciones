from django.db.models import Model, CharField, ImageField, SlugField, ForeignKey, CASCADE, DateTimeField
from ckeditor.fields import RichTextField
from news.models import Category, Autor


class News(Model):
    title = CharField(max_length=100)
    slug = SlugField(max_length=120)
    category = ForeignKey(Category, on_delete=CASCADE)
    autor = ForeignKey(Autor, on_delete=CASCADE)
    image = ImageField(upload_to='news')
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
