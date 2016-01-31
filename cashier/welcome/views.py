from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import pdb


class Welcome(TemplateView):
    template_name = 'welcome.html'


def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['email'], email=request.POST['email'],
                                        password=request.POST['password'],
                                        first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        user.save()
        return redirect('/welcome/')


def log_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail'})


def log_out(request):
    logout(request)
    return redirect('/welcome/')


class fail(TemplateView):
    template_name = 'logout.html'
