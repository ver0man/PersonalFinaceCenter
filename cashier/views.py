from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from .models import *
from .forms import *
import pdb


class Dashboard(LoginRequiredMixin, TemplateView):
    login_url = '/logout/'
    template_name = 'dashboard/dashboard.html'


def statistics_data(request):
    """
    Serve data to dashboard, statistics highcharts.
    If total < 0, show it in 0 in the plot.
    :return: Json of plot data.
    """
    data, wallets = {}, Wallet.objects.filter(wallet_person=request.user)[:]
    data['xAxis'], data['income'], data['expense'], data['total'] = [], [], [], []
    for wallet in wallets:
        data['xAxis'].append(wallet.wallet_name)
        data['income'].append(wallet.wallet_income)
        data['expense'].append(wallet.wallet_expense)
        data['total'].append(wallet.wallet_total)

    return JsonResponse(data)


def contrast_data(request):
    data, wallets = {}, Wallet.objects.filter(wallet_person=request.user)[:]
    data['total'] = []
    total = sum([wallet.wallet_total if wallet.wallet_total > 0 else 0 for wallet in wallets])
    for wallet in wallets:
        share = wallet.wallet_total / total if wallet.wallet_total > 0 else 0
        data_point = {'name': wallet.wallet_name, 'y': share}
        data['total'].append(data_point)

    return JsonResponse(data)


class GetWallet(TemplateView):
    """
    For fetch wallet data and show in color, extended by some ajax code.
    """
    template_name = 'dashboard/wallet.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GetWallet, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the wallets
        context['user_id'] = self.request.user.id
        context['wallet_list'] = Wallet.objects.filter(wallet_person=self.request.user).order_by('wallet_name')[:]
        return context


def modify_wallet(request):
    """
    For create, update, or delete wallet.
    :return: redirect to previous page.
    """
    wallet_form = WalletForm(request.POST)
    if wallet_form.is_valid():
        if 'add_wallet' in request.POST:
            wallet_form.save()
        elif 'delete_wallet' in request.POST:
            wallet = Wallet.objects.filter(wallet_person=request.user, wallet_name=request.POST['wallet_name'])
            wallet.delete()
        elif 'update_wallet' in request.POST:
            wallet = wallet_form.save(commit=False)
            wallet.wallet_total = request.POST['wallet_total']
            wallet.wallet_note = request.POST['wallet_note']
            wallet.save()

    return redirect('/wallet/wallet/')


def get_wallet(request, wallet_id):
    """
    For AJAX query.
    """
    wallet = Wallet.objects.get(id=wallet_id)
    return JsonResponse({
        'name': wallet.wallet_name,
        'total': wallet.wallet_total,
        'note': wallet.wallet_note,
    })


class Earn(LoginRequiredMixin, TemplateView):
    """
    For add earning money into wallet.
    """
    template_name = 'dashboard/earn.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Earn, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the wallets
        context['wallet_list'] = Wallet.objects.filter(wallet_person=self.request.user).order_by('wallet_name')[:]
        return context


class Expend(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/expend.html'

    def get_context_data(self, **kwargs):
        context = super(Expend, self).get_context_data(**kwargs)

        # Same QuerySet
        context['wallet_list'] = Wallet.objects.filter(wallet_person=self.request.user).order_by('wallet_name')[:]
        return context


def add_income(request):
    """
    Add money. Update the wallet simultaneously.
    :param request:
    :return:
    """
    if request.method == 'POST':
        wallets = Wallet.objects.filter(wallet_person=request.user)[:]
        for wallet in wallets:
            post_amount_name = wallet.wallet_name + "amount"
            post_amount = request.POST[post_amount_name]
            if post_amount != '':
                # Update wallet data
                wallet.wallet_income += float(post_amount)
                wallet.wallet_total += float(post_amount)
                wallet.save()

                # Update income data

                income = Income(income_person=request.POST['name'], income_wallet_id=wallet.id,
                                income_amount=float(post_amount), income_text=request.POST['text'])
                income.save()

        return redirect('/wallet/income/')


def add_expense(request):
    if request.method == 'POST':
        wallets = Wallet.objects.filter(wallet_person=request.user)[:]
        for wallet in wallets:
            post_amount_name = wallet.wallet_name + "amount"
            post_amount = request.POST[post_amount_name]
            if post_amount != '':
                # Update wallet data
                wallet.wallet_expense += float(post_amount)
                wallet.wallet_total -= float(post_amount)
                wallet.save()

                # Update expense data
                expense = Expense(expense_person=request.POST['name'], expense_wallet_id=wallet.id,
                                  expense_amount=float(post_amount), expense_text=request.POST['text'])
                expense.save()

        return redirect('/wallet/expense/')


class Detail(TemplateView):
    template_name = 'dashboard/detail.html'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        wallets = Wallet.objects.filter(wallet_person=self.request.user)[:]
        income_list, expense_list = [], []
        for wallet in wallets:
            income_list.extend(Income.objects.filter(income_wallet=wallet)[:])
            expense_list.extend(Expense.objects.filter(expense_wallet=wallet)[:])

        context['income_list'] = income_list
        context['expense_list'] = expense_list

        return context
