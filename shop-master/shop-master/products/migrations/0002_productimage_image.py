# Generated by Django 3.0.7 on 2020-07-02 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField( upload_to='products_images/'),
            preserve_default=False,
        ),
    ]
