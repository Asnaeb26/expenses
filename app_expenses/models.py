from django.contrib.auth.models import User
from django.db import models


# ---------------------Incomes-----------------------------------
# class BlackListedToken(models.Model):
#     token = models.CharField(max_length=500)
#     user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         unique_together = ("token", "user")


class IncomeCategory(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=50)  # цвет в формате #01FA22

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_source')

    def __str__(self):
        return self.name


class Income(models.Model):
    created = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='income')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')

    def __str__(self):
        return f'Доход №{self.id} {self.amount} "BYN"'


# ---------------------Expenses-----------------------------------


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=20)
    nameRusCase = models.CharField(max_length=20)
    color = models.CharField(max_length=50)  # цвет в формате #01FA22

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')

    def __str__(self):
        return self.name


class Expense(models.Model):
    created = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expenses')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')

    def __str__(self):
        return f'Расход №{self.id} {self.amount} "BYN"'


# ------------------------------------------------------------------


class Relativity(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relativity')

    def __str__(self):
        return f'Относительная величина - {self.name}'


class RelativeCase(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    relativity = models.OneToOneField(Relativity, on_delete=models.CASCADE, related_name='case')


class Client(models.Model):
    salary_day = models.IntegerField()
    salary_month = models.IntegerField()
    source = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='client')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_client')

    def __str__(self):
        return f'№ {self.source_id} {self.source}'
