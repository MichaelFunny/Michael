# Generated by Django 3.0.7 on 2020-06-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200625_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True, verbose_name='productid')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование товара')),

                ('quanity', models.CharField(max_length=50, verbose_name='Количество товара на складе')),
                ('cost', models.CharField(max_length=50, verbose_name='Цена за единицу товара')),
            ],
        ),

        migrations.DeleteModel(
            name='Products',
        ),
    
    ]