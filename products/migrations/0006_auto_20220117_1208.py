# Generated by Django 3.2.7 on 2022-01-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_cart_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/category', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products', verbose_name='Картинка'),
        ),
    ]
