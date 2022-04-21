from django.contrib.auth.models import User
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


class Category(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=7)  # цвет в формате #01FA22
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.name


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODE, default='BYN')  # формат 'USD', 'BYN'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_income')
    created = models.CharField(max_length=50)


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODE, default='BYN')  # формат 'USD', 'BYN'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_expense')
    created = models.CharField(max_length=50)


class Relativity(models.Model):
    name = models.CharField(max_length=50, choices=VALUE)
    amount = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relativity')


class Client(models.Model):
    salary_day = models.IntegerField(default=1)
    created = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_client')
