from django.urls import path
from users.views import (UserRegisterView, ProfileView, verify_mail, UserForgotPasswordView, GenerateNewPassword,
                         generate_new_password)
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('reset_password/', UserForgotPasswordView.as_view(), name='reset_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='reg'),
    path('verification_code/<str:code>/', verify_mail, name='verification_code'),
    path('profile/edit/', ProfileView.as_view(), name='profile'),
    path('set_new_password/<uidb64>/<token>/', GenerateNewPassword.as_view(), name='set_new_password'),
    path('profile/new_pass', generate_new_password, name='new_pass')
]
