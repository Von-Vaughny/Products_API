# Generated by Django 4.0.5 on 2022-06-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
