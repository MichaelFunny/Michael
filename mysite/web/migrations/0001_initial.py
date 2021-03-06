# Generated by Django 3.0.7 on 2020-06-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование товара')),
                ('brand', models.CharField(choices=[('huawei', 'Huawei'), ('dexp', 'Dexp'), ('apple', 'Apple'), ('nokia', 'Nokia'), ('electrolux', 'Electolux')], max_length=20)),
                ('category', models.CharField(choices=[('телефон', 'Телефон'), ('наушники', 'Наушники'), ('холодильник', 'Холодильник')], max_length=20)),
                ('quanity', models.CharField(max_length=50, verbose_name='Количество')),
                ('cost', models.CharField(max_length=50, verbose_name='Цена')),
            ],
        ),
    ]
