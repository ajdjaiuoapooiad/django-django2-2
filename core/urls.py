from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('post/<int:pk>',views.detail,name='detail'),
]