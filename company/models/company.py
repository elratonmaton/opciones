from django.db.models import Model, CharField, ImageField, TextField, SlugField
from django.utils.text import slugify


class Company(Model):
    name = CharField(max_length=100)
    slug = SlugField(max_length=200)
    heading = CharField(max_length=100)
    home_link_more = CharField(max_length=100)
    home_logo = ImageField(upload_to='company/logos')
    image_block_1 = ImageField(upload_to='company/blocks', blank=True, null=True)
    block_1_video = CharField(max_length=250, blank=True, null=True, help_text='id del video de youtube')
    description_title = TextField(help_text='descripcion con tamaño mayor para Opciones', blank=True, null=True)
    description = TextField(help_text='descripcion para home y primer bloque menor tamaño', blank=True, null=True)

    middle_message = TextField(help_text='mensaje entre bloque y bloque', blank=True, null=True)

    image_block_2 = ImageField(upload_to='company/blocks', blank=True, null=True)
    description_title_block_2 = TextField(help_text='descripcion con tamaño mayor para Opciones', blank=True, null=True)
    description_block_2 = TextField(help_text='descripcion para el bloque 2', null=True, blank=True)

    title_block_3 = CharField(max_length=100, blank=True, null=True)
    image_block_3 = ImageField(upload_to='company/blocks', blank=True, null=True)
    background_block_3 = ImageField(upload_to='company/blocks', blank=True, null=True)
    logo_company_block_3 = ImageField(upload_to='company/blocks', blank=True, null=True)
    description_title_block_3 = TextField(blank=True, null=True)
    description_block_3 = TextField(blank=True, null=True)

    icon_1_block_4 = ImageField(upload_to='company/blocks', blank=True, null=True)
    title_1_block_4 = CharField(max_length=100, blank=True, null=True)
    description_1_block_4 = TextField(blank=True, null=True)
    icon_2_block_4 = ImageField(upload_to='company/blocks', blank=True, null=True)
    title_2_block_4 = CharField(max_length=100, blank=True, null=True)
    description_2_block_4 = TextField(blank=True, null=True)
    icon_3_block_4 = ImageField(upload_to='company/blocks', blank=True, null=True)
    title_3_block_4 = CharField(max_length=100, blank=True, null=True)
    description_3_block_4 = TextField(blank=True, null=True)

    company_web_page_link = CharField(max_length=250, blank=True, null=True)
    company_web_page_name = CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Company, self).save(*args, **kwargs)
