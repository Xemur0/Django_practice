from django.db import models

# Create your models here.
CURRENCY_CHOICES = [
    ('USD', 'Usd'),
    ('EUR', 'Eur'),
    ('RUB', 'Rub'),
]


class Good(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование товара')
    come_date = models.DateTimeField(auto_now_add=True,
                                     verbose_name='Дата поступления')
    price = models.FloatField(blank=False, null=True,
                              help_text="Обязательно к заполнению",
                              verbose_name='Цена')
    provider = models.CharField(max_length=64, verbose_name='Имя поставщика')
    unit_of_price = models.CharField(max_length=3, choices=CURRENCY_CHOICES,
                                     verbose_name='Единица измерения')
    category = models.ManyToManyField('Category', blank=False,
                                      verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class Category(models.Model):
    title = models.CharField(max_length=64)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title