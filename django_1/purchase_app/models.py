from django.db import models
from user_app.models import User
from book_app.models import Book

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'purchase'