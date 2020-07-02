# Generated by Django 3.0.7 on 2020-06-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_s', models.CharField(max_length=50, verbose_name='Имя продавца')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(choices=[('huawei', 'Huawei'), ('dexp', 'Dexp'), ('apple', 'Apple'), ('nokia', 'Nokia'), ('electrolux', 'Electolux')], max_length=20, verbose_name='Брэнд'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField( max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='products',
            name='cost',
            field=models.CharField(max_length=50, verbose_name='Цена за единицу товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='quanity',
            field=models.CharField(max_length=50, verbose_name='Количество товара на складе'),
        ),
    ]
