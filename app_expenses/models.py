# from django.contrib.auth.models import User
from django.db import models


# ---------------------Incomes-----------------------------------


class IncomeCategory(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=50)  # цвет в формате #01FA22

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.name


class Income(models.Model):
    created = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='income')

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')

    def __str__(self):
        return f'Доход №{self.id} {self.amount} "BYN"'


# ---------------------Expenses-----------------------------------


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=20)
    nameRusСase = models.CharField(max_length=20)
    color = models.CharField(max_length=50)  # цвет в формате #01FA22
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.name


class Expense(models.Model):
    created = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expenses')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')

    def __str__(self):
        return f'Расход №{self.id} {self.amount} "BYN"'


# ------------------------------------------------------------------


class Relativity(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    amount = models.FloatField(default=0)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relativity')


class Client(models.Model):
    salary_day = models.CharField(max_length=10)
    source = models.OneToOneField(IncomeCategory, on_delete=models.CASCADE, related_name='client')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_client')
