from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminCreateForm
from products.models import ProductCategory


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Ползователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UsersListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'Ползователи',
#         'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)


class UsersCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание ползователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UsersCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'Создание ползователя',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)


class UsersUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UsersUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование ползователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UsersUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#
#     form = UserAdminProfileForm(instance=selected_user)
#     context = {
#         'title': 'Редактирование ползователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_remove(request, pk):
#     user = User.objects.get(id=pk)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_read(request):
#     context = {
#         'title': 'Категории',
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'admins/admin-category-read.html', context)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryAdminCreateForm
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category_read')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category_read'))
#     else:
#         form = CategoryAdminCreateForm()
#     context = {
#         'title': 'Добавление категории.',
#         'form': form,
#     }
#     return render(request, 'admins/admin-category-create.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = CategoryAdminCreateForm
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category_read')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование категории товара'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_update(request, pk):
#     selected_cat = ProductCategory.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(instance=selected_cat, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category_read'))
#     else:
#         form = CategoryAdminCreateForm(instance=selected_cat)
#     context = {
#         'title': 'Редактирование категории товара.',
#         'form': form,
#         'selected_cat': selected_cat,
#     }
#     return render(request, 'admins/admin-category-update-delete.html', context)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category_read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_staff)
# def admin_category_remove(request, pk):
#     category = ProductCategory.objects.get(id=pk)
#     category.delete()
#     return HttpResponseRedirect(reverse('admins:admin_category_read'))
