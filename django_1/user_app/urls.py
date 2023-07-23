from django.urls import path
from .views import UserListView, UserDetailView, CreateUserView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('<int:id>/', UserDetailView.as_view(), name='user_detail'),
]
