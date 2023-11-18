from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import random


# Create your views here.
class UserRegisterView(CreateView):
    """
    Контроллер регистрации пользователя
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/reg.html'

    def form_valid(self, form):
        """
        Верификация почты по ссылке
        """
        new_user = form.save()
        code = ''.join(random.sample('0123456789', 4))
        new_user.verification_code = code
        # new_user.is_active = False
        send_mail(
            subject='Верификация SkyStore',
            message=f'''Перейдите по ссылке для верификации: http://127.0.0.1:8000/users/verification_code/{code}
и введите Логин и пароль''',
            from_email=EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verification(request, code):
    """
    Контроллер верификации email
    """
    user = User.objects.get(verification_code=code)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    """
    Контроллер редактирования профиля пользователя
    """
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        """
        Чтобы не передавать pk
        """
        return self.request.user


def generate_new_password(request):
    """
    Контроллер генерации нового пароля и отправка его на почту
    """
    new_password = User.objects.make_random_password()
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль для авторизации: {new_password}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    messages.success(request, 'Вам на почту отправлено письмо с новым паролем для вашего аккаунта')
    return redirect(reverse('users:login'))
