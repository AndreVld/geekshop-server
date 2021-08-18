from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from common.views import ContextMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileInfoForm
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

from users.models import User


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.is_activation_key_not_expired() and user.activation_key == activation_key:
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'users/verification.html')
    except Exception as err:
        print(f'error activation user : {err.args}')
        return HttpResponseRedirect(reverse('index'))


class LoginUserView(ContextMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Авторизация'


class RegistrationView(ContextMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    title = 'GeekShop - Регистрация'
    success_url = reverse_lazy('index')
    success_message = 'Электронное письмо для подтверждения аккаунта отправленно на вашу почту!'

    def form_valid(self, form):
        response = super(RegistrationView, self).form_valid(form)
        form.send_verify_email()
        return response


class ProfileUserView(ContextMixin, UpdateView):
    form_class = UserProfileForm
    info_form = UserProfileInfoForm
    template_name = 'users/profile.html'
    model = User
    title = 'GeekShop - Личный кабинет'

    def get(self, request, *args, **kwargs):
        super(ProfileUserView, self).get(request, *args, **kwargs)
        form = self.form_class(instance=request.user)
        user_info_form = self.info_form(instance=request.user.userprofileinfo)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['user_info_form'] = user_info_form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        super(ProfileUserView, self).post(request, *args, **kwargs)
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        user_info_form = self.info_form(request.POST, instance=request.user.userprofileinfo)
        if form.is_valid() and user_info_form.is_valid():
            form.save()
            messages.success(request, 'Все измененеия сохранены.')
        return self.render_to_response(self.get_context_data(form=form, user_info_form=user_info_form))

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class UserLogoutView(LogoutView):
    pass

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

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
