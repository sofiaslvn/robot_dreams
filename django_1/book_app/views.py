# from django.http import JsonResponse
# from .models import Book
#
# def get_books(request):
#     books = Book.objects.all()
#     book_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
#     return JsonResponse({'books': book_list})

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        return render(request, 'book_detail.html', {'book': book})