# Generated by Django 3.2.9 on 2021-12-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainchop', '0002_auto_20211217_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
    ]
