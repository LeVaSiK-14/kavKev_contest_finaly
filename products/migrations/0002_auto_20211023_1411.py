# Generated by Django 3.2.7 on 2021-10-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sum_price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В ожидании доставки', 'In Pending'), ('Успешно доставлен', 'Succsess'), ('Отменён', 'Canceled')], default='В ожидании доставки', max_length=50),
        ),
    ]
