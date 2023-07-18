from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)

    class Meta:
        db_table = 'user'


class Passport(models.Model):
    number = models.CharField(max_length=10)
    issued = models.DateField(null=False)
    expires = models.DateField(null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'passport'
        ordering = ('-issued', 'number')