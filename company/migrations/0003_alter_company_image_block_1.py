# Generated by Django 3.2.7 on 2021-09-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_block_1_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image_block_1',
            field=models.ImageField(blank=True, null=True, upload_to='company/blocks'),
        ),
    ]
