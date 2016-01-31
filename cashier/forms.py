from django.forms import ModelForm, PasswordInput
from .models import *


class WalletForm(ModelForm):

    class Meta:
        model = Wallet
        fields = ['wallet_person', 'wallet_name', 'wallet_total', 'wallet_note']


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


