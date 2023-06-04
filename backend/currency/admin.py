from django.contrib import admin

from . import models

admin.site.register(models.CurrencyName)
admin.site.register(models.CurrencyDate)
admin.site.register(models.CurrencyValue)
