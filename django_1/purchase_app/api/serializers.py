from rest_framework import serializers
from purchase_app.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

        # >> > from purchase_app.serializers import PurchaseSerializer
        # >> > from purchase_app.models import Purchase
        # >> > purchase = Purchase.objects.first()
        # >> > serializer = PurchaseSerializer(purchase)
        # >> > serializer
