from django.contrib import admin

# Register your models here.
from .models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'come_date', 'price', 'provider', 'unit_of_price')
    list_display_links = ('name', )


admin.site.register(Good, GoodAdmin)
