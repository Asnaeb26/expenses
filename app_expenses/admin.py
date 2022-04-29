from django.contrib import admin

from . import models

admin.site.register(models.IncomeCategory)
admin.site.register(models.Income)
admin.site.register(models.ExpenseCategory)
admin.site.register(models.Expense)
admin.site.register(models.Client)
admin.site.register(models.Relativity)
admin.site.register(models.RelativeCase)