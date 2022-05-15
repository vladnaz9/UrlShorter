from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('showAll/', views.showAll),
]
