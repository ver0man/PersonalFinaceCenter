from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Client)
admin.site.register(Wallet)
admin.site.register(Income)
admin.site.register(Expense)
