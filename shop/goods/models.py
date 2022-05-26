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

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
