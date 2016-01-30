"""Wallet-Cashier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'^statistics/$', statistics_data, name='statistics'),
    url(r'^contrast/$', contrast_data, name='contrast'),

    url(r'^wallet/$', GetWallet.as_view(), name='wallet'),
    url(r'^wallet/modify/$', modify_wallet, name='modify_wallet'),
    url(r'^wallet/get/(?P<wallet_id>[0-9]+)/$', get_wallet, name='get_wallet'),

    url(r'^income/$', Earn.as_view(), name='income'),
    url(r'^income/add/$', add_income, name='add_income'),

    url(r'^expense/$', Expend.as_view(), name='expense'),
    url(r'^expense/add/$', add_expense, name='add_expense'),

    url(r'^detail/$', Detail.as_view(), name='detail'),
]
