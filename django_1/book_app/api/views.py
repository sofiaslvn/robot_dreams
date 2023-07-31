from rest_framework.viewsets import ModelViewSet
from book_app.models import Book
from book_app.api.serializers import BookSerializer



class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ('__all__')