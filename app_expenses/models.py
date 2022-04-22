# from django.contrib.auth.models import User
from django.db import models

CURRENCY_CODE = [
    ('BYN', 'Белорусский рубль'),
    ('USD', 'Доллар'),
    ('EUR', 'Евро'),
]

VALUE = [
    ('Штука', 'шт'),
    ('Литр', 'л'),
    ('Бутылка', 'бут'),
    ('Килограмм', 'кг'),
    ('Пара', 'пар'),
    ('Пачка', 'пачка'),
]


class IncomeCategory(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=50)  # цвет в формате #01FA22

    # income = models.ForeignKey(Income, on_delete=models.CASCADE, related_name='income_category')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.name


class Income(models.Model):
    created = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODE, default='BYN')  # формат 'USD', 'BYN'
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='category_income')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')

    def __str__(self):
        return f'Доход {self.amount} {self.currency}'


class Expense(models.Model):
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODE, default='BYN')  # формат 'USD', 'BYN'
    created = models.CharField(max_length=50)
    # category = models.ForeignKey(!!Category, on_delete=models.CASCADE, related_name='category_expense')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')


# ------------------------------------------------------------------


class Relativity(models.Model):
    name = models.CharField(max_length=50, choices=VALUE)
    amount = models.FloatField(default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relativity')


class Client(models.Model):
    salary_day = models.IntegerField(default=1)
    created = models.CharField(max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_client')
