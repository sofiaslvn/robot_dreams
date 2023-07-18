from django.shortcuts import render
from django.http import HttpResponse



def greetings_to_users(request):
    return HttpResponse('Hello, users!')
