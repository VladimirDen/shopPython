# Generated by Django 3.2.9 on 2021-12-12 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pomp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименнование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изоброжение товара')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('brend', models.CharField(max_length=50, verbose_name='Фирма')),
                ('tape', models.CharField(max_length=60, verbose_name='Тип')),
                ('appointment', models.CharField(max_length=25, verbose_name='Назначение')),
                ('power', models.CharField(max_length=25, verbose_name='Потребляемая мощность')),
                ('max_head', models.CharField(max_length=15, verbose_name='Максимальный напор')),
                ('throughput', models.CharField(max_length=10, verbose_name='Пропускная способность')),
                ('max_bar', models.CharField(max_length=5, verbose_name='Макс. рабочее давление')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainchop.category', verbose_name='Категория товара')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='mainchop.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainchop.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainchop.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_card', to='mainchop.CartProduct'),
        ),
        migrations.CreateModel(
            name='Boiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименнование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изоброжение товара')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('brend', models.CharField(max_length=50, verbose_name='Фирма')),
                ('power', models.CharField(max_length=50, verbose_name='Мощность котла')),
                ('fuel_type', models.CharField(max_length=255, verbose_name='Тип топлива')),
                ('installation_method', models.CharField(max_length=100, verbose_name='Способ монтажа')),
                ('presence_contours', models.CharField(max_length=3, verbose_name='Колличество контуров')),
                ('combustion_chamber', models.CharField(max_length=10, verbose_name='Камера сгорания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainchop.category', verbose_name='Категория товара')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
