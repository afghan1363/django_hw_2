from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, View
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from catalog.forms import StyleFormMixin
import random
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView


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
        send_mail(
            subject='Верификация SkyStore',
            message=f'''Перейдите по ссылке для верификации: http://127.0.0.1:8000/users/verification_code/{code}
и введите Логин и пароль''',
            from_email=EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verify_mail(request, code):
    """
    Контроллер верификации email
    """
    user = User.objects.get(verification_code=code)
    user.is_active = True
    user.save()
    messages.success(request, 'Ваш аккаунт активирован!')
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


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = PasswordResetForm
    from_email = EMAIL_HOST_USER
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Письмо с новым паролем отправлено на ваш email'
    # subject_template_name = 'Восстановление пароля на сайте SkyStore'
    email_template_name = 'users/mail_password_reset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


def generate_new_password(request):
    """
    Контроллер генерации нового пароля и отправка его на почту
    """
    new_password = User.objects.make_random_password()
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Изменение пароля',
        message=f'Ваш новый пароль для авторизации: {new_password}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    messages.success(request, 'Вам на почту отправлено письмо с новым паролем для вашего аккаунта')
    return redirect(reverse('users:login'))


class GenerateNewPassword(SuccessMessageMixin, View):
    """
    Контроллер восстановления генерации пароля, если пользователь забыл свой пароль
    """
    def get(self, request, uidb64: str, token: str):
        user = self.get_user(uidb64)
        from django.contrib.auth.tokens import default_token_generator
        if not user or not default_token_generator.check_token(user, token):
            messages.warning(self.request, 'Ошибка подтверждения, попробуйте ещё раз.')
        else:
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль для авторизации: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            messages.success(request, 'Вам на почту отправлено письмо с новым паролем для вашего аккаунта')
            return redirect(reverse('users:login'))

    @staticmethod
    def get_user(uid_base64: str) -> User | None:
        try:
            from django.utils.http import urlsafe_base64_decode
            uid = urlsafe_base64_decode(uid_base64).decode()
            user_id = int(uid)
            user = User.objects.get(pk=user_id)
        except (ValueError, User.DoesNotExist):
            user = None
        return user

