from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     """
#     For simple user admin.
#     """
#     user_firstname = models.CharField(max_length=20)
#     user_lastname = models.CharField(max_length=20)
#     user_email = models.EmailField(unique=True)
#     user_password = models.CharField(max_length=20)
#     user_tel = models.CharField(max_length=15)
#     user_add_time = models.DateTimeField(auto_now_add=True)


class Wallet(models.Model):
    """
    Serve as different types of wallets or repos.
    """
    wallet_person = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=30)
    wallet_income = models.FloatField(default=0)
    wallet_expense = models.FloatField(default=0)
    wallet_total = models.FloatField(default=0)
    wallet_note = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['wallet_name']

    def __str__(self):
        return self.wallet_name


class Income(models.Model):
    income_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    income_person = models.CharField(max_length=30)
    income_time = models.DateTimeField(auto_now_add=True)
    income_amount = models.FloatField(default=0)
    income_text = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-income_time', 'income_person']


class Expense(models.Model):
    expense_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    expense_person = models.CharField(max_length=30)
    expense_time = models.DateTimeField(auto_now_add=True)
    expense_amount = models.FloatField(default=0)
    expense_text = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-expense_time', 'expense_person']
