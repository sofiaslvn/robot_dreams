# from django.http import JsonResponse
# from .models import Purchase
#
# def get_purchases(request):
#     purchases = Purchase.objects.all()
#     purchase_list = [{'id': purchase.id, 'user_id': purchase.user.id, 'book_id': purchase.book.id, 'quantity': purchase.quantity} for purchase in purchases]
#     return JsonResponse({'purchases': purchase_list})

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Purchase

class PurchaseListView(View):
    def get(self, request):
        purchases = Purchase.objects.all()
        return render(request, 'purchase_list.html', {'purchases': purchases})

class PurchaseDetailView(View):
    def get(self, request, id):
        purchase = get_object_or_404(Purchase, id=id)
        return render(request, 'purchase_detail.html', {'purchase': purchase})