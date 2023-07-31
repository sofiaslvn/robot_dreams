# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.get_books, name='get_books'),
# ]

from django.urls import path
from .views import BookListView, BookDetailView
from book_app import views
from rest_framework.routers import SimpleRouter
from book_app.api import views as api_views


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
]


router = SimpleRouter()
router.register('api', api_views.BookModelViewSet)
urlpatterns += router.urls