from django.contrib import admin

from . import models

admin.site.register(models.IncomeCategory)
admin.site.register(models.Income)