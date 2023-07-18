from django.http import JsonResponse
from .models import Purchase

def get_purchases(request):
    purchases = Purchase.objects.all()
    purchase_list = [{'id': purchase.id, 'user_id': purchase.user.id, 'book_id': purchase.book.id, 'quantity': purchase.quantity} for purchase in purchases]
    return JsonResponse({'purchases': purchase_list})