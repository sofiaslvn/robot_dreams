# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.get_purchases, name='get_purchases'),
# ]

from django.urls import path
from .views import PurchaseListView, PurchaseDetailView
from rest_framework.routers import SimpleRouter
from purchase_app.api import views as api_views

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]

router = SimpleRouter()
router.register('api', api_views.PurchaseModelViewSet)
urlpatterns += router.urls