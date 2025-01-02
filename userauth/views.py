from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userauth.forms import RegisterForm

# Create your views here.
class register(CreateView):
    form_class=RegisterForm
    template_name='userauth/register.html'
    success_url=reverse_lazy('index')