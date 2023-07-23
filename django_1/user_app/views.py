from django.http import JsonResponse
from .models import User

def get_users(request):
    users = User.objects.all()
    user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return JsonResponse({'users': user_list})