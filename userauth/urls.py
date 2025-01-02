from django.contrib import admin
from django.urls import include, path

from userauth import views

urlpatterns = [
    path('register',views.register.as_view(),name='register'),
    path('',views.login.as_view(),name='login'),
]