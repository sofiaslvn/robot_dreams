from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'My super user'
        verbose_name_plural = 'My super users'


class Passport(models.Model):
    number = models.CharField(max_length=10)
    issued = models.DateField(null=False)
    expires = models.DateField(null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'passport {self.id} number:{self.number}'

    class Meta:
        db_table = 'passport'
        ordering = ('-issued', 'number')