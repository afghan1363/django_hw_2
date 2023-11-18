from django.urls import path
from users.views import UserRegisterView, ProfileView, verification
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='reg'),
    path('verification_code/<str:code>/', verification, name='verification_code'),
    path('profile/edit/', ProfileView.as_view(), name='profile'),
]
