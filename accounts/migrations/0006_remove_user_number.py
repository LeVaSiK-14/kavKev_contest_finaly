# Generated by Django 3.2.7 on 2021-12-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
    ]
