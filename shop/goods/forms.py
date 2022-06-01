from django import forms

from django.core import validators

from .models import Good, Category


class GoodForm(forms.ModelForm):
    CURRENCY_CHOICES = [
        ('USD', 'Usd'),
        ('EUR', 'Eur'),
        ('RUB', 'Rub'),
    ]



    name = forms.CharField(label='Название товара',
                           validators=[validators.RegexValidator(regex='^.{3,}$')],
                           error_messages={'invalid':
                                               'Слишком короткое '
                                               'название товара'})

    price = forms.DecimalField(label='Цена', decimal_places=2)
    unit_of_price = forms.ChoiceField(choices=CURRENCY_CHOICES,
                                      label='Единица измерения')
    category = forms.ModelMultipleChoiceField(label='Категории',
                                         queryset=Category.objects.all(),
                                        widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Good
        fields = ('name', 'price', 'provider', 'unit_of_price', 'category')
