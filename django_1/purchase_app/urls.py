# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.get_purchases, name='get_purchases'),
# ]

from django.urls import path
from .views import PurchaseListView, PurchaseDetailView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]