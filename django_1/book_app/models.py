from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f'Id {self.id}; Title: {self.title}; Author: {self.author}'