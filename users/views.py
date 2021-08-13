from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from common.views import DataMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

from users.models import User


class LoginUserView(DataMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Авторизация'


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'GeekShop - Авторизация',
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)


class RegistrationView(DataMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались'
    title = 'GeekShop - Регистрация'


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {
#         'title': 'GeekShop - Регистрация',
#         'form': form,
#     }
#     return render(request, 'users/registration.html', context)


class ProfileUserView(DataMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    model = User
    title = 'GeekShop - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Все измененеия сохранены.')
#             return HttpResponseRedirect(reverse('users:profile'))
#
#     form = UserProfileForm(instance=request.user)
#     context = {
#         'title': 'GeekShop - Личный кабинет',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user)
#     }
#     return render(request, 'users/profile.html', context)
#
#

class UserLogoutView(LogoutView):
    pass

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
