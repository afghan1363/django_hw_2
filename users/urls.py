from django.urls import path
from users.views import UserRegisterView
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'users'
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='reg'),
]
