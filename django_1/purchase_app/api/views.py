from rest_framework.viewsets import ModelViewSet
from purchase_app.models import Purchase
from purchase_app.api.serializers import PurchaseSerializer



class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_fields = ('__all__')