from django.urls import path
from .views import UserListView, UserDetailView, CreateUserView
from rest_framework.routers import SimpleRouter
from user_app.api import views as api_views

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('<int:id>/', UserDetailView.as_view(), name='user_detail'),
]

router = SimpleRouter()
router.register('api', api_views.UserModelViewSet)
urlpatterns += router.urls