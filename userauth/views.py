from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView

from userauth.forms import LoginForm, RegisterForm

# Create your views here.
class register(CreateView):
    form_class=RegisterForm
    template_name='userauth/register.html'
    success_url=reverse_lazy('index')
    
class login(LoginView):
    form_class=LoginForm
    template_name='userauth/login.html'