# Generated by Django 3.2.7 on 2021-12-20 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_token_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='user',
        ),
        migrations.CreateModel(
            name='UserTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.token')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
