from django.db import models
from user_app.models import User
from book_app.models import Book

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}; User: {self.user_id}; Book: {self.book_id}; Quantity  {self.quantity}"

    class Meta:
        db_table = 'purchase'