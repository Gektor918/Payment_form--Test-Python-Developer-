# Generated by Django 4.1.3 on 2022-11-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(max_length=8, verbose_name='Цена'),
        ),
    ]
