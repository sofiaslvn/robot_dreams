from rest_framework import serializers
from book_app.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        # >> > from book_app.serializers import BookSerializer
        # >> > from book_app.models import Book
        # >> > book = Book.objects.first()
        # >> > serializer = BookSerializer(book)
