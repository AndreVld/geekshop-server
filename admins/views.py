from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminCreateForm
from django.contrib.auth.decorators import user_passes_test
from products.models import ProductCategory


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'Ползователи',
        'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Создание ползователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))

    form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Редактирование ползователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_remove(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_staff)
def admin_category_read(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryAdminCreateForm()
    context = {
        'title': 'Добовление категории.',
        'form': form,
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_update(request, pk):
    selected_cat = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryAdminCreateForm(instance=selected_cat, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryAdminCreateForm(instance=selected_cat)
    context = {
        'title': 'Редактирование категории товара.',
        'form': form,
        'selected_cat': selected_cat,
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_remove(request, pk):
    category = ProductCategory.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_category_read'))
