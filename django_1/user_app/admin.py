from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user_app.models import Passport
from django.contrib import admin

admin.site.register(get_user_model())
admin.site.register(Passport)
# @admin.register(get_user_model())
# class UserAdmin(UserAdmin):
#     pass