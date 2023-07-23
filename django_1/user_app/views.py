# from django.http import JsonResponse
# from .models import User
#
# def get_users(request):
#     users = User.objects.all()
#     user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
#     return JsonResponse({'users': user_list})

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import User
from .forms import UserForm

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            return render(request, 'user_detail.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'user_not_found.html')

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user_form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user_form.html', {'form': form})