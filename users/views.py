from django.shortcuts import render
from django.views.generic import CreateView
from users.models import User
from users.forms import UserForm
from django.urls import reverse_lazy


# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/reg.html'



