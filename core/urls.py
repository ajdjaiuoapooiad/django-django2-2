from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('post/<int:pk>',views.detail,name='detail'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    
    # 
    path('like/<int:pk>',views.like,name='like'),
]