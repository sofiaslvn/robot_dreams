from django.http import JsonResponse
from .models import Book

def get_books(request):
    books = Book.objects.all()
    book_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return JsonResponse({'books': book_list})