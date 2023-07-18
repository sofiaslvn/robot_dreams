from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_purchases, name='get_purchases'),
]