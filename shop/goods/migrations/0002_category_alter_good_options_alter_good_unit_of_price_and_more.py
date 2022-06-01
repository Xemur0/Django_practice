# Generated by Django 4.0.4 on 2022-05-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='good',
            name='unit_of_price',
            field=models.CharField(choices=[('USD', 'Usd'), ('EUR', 'Eur'), ('RUB', 'Rub')], max_length=3, verbose_name='Единица измерения'),
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ManyToManyField(to='goods.category', verbose_name='Категория'),
        ),
    ]
