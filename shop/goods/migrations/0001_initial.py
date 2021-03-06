# Generated by Django 4.0.4 on 2022-05-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование товара')),
                ('come_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')),
                ('price', models.FloatField(help_text='Обязательно к заполнению', null=True, verbose_name='Цена')),
                ('provider', models.CharField(max_length=64, verbose_name='Имя поставщика')),
                ('unit_of_price', models.CharField(choices=[('USD', 'Usd'), ('EUR', 'Eur'), ('RUB', 'Rub')], max_length=3)),
            ],
        ),
    ]
