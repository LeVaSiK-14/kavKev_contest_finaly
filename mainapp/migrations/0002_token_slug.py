# Generated by Django 3.2.7 on 2021-10-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='slug',
            field=models.SlugField(default='', max_length=127),
        ),
    ]
