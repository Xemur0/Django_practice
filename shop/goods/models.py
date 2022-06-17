from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.
from django.db.models import Manager



CURRENCY_CHOICES = [
    ('USD', 'Usd'),
    ('EUR', 'Eur'),
    ('RUB', 'Rub'),
]


class DeletedQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db)


class CurrentSiteManagerDeleted(CurrentSiteManager):
    """Пытался тут одновременно и фильтрацию по сайту и по удаленным"""
    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db)


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
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False, null=False)

    objects = DeletedManager()
    # current_site = CurrentSiteManagerDeleted('site')
    current_site = CurrentSiteManager('site')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    current_site = CurrentSiteManager('site')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
