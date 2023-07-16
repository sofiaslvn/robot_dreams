from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.greetings_to_users)
]