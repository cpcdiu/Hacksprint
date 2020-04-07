from django.conf.urls import url
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminpanel/index.html')


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    all_user = User.objects.all().order_by('-date_joined')
    return render(request, 'adminpanel/users.html', {'users': all_user})


@user_passes_test(lambda u: u.is_superuser)
def settings(request):
    return render(request, 'adminpanel/settings.html')


@user_passes_test(lambda u: u.is_superuser)
def user_action(request, action, uid):
    if action == 'approve':
        user = User.objects.filter(id=uid)
        user.update(is_active=True)

    if action == 'delete':
        user = User.objects.filter(id=uid)
        user.delete()
    return redirect('admin-users')


def admin_login(request):
    if request.method == 'GET':
        return render(request, 'adminpanel/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('adminpanel')
        else:
            messages.error(request, 'No such account')
            return render(request, 'adminpanel/login.html')
