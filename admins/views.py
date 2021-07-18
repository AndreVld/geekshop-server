from django.shortcuts import render
from users.models import User


def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update_delete(request):
    return render(request, 'admins/admin_users_update_delete.html', context)
