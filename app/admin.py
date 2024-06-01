from django.contrib import admin
from .models import insert_movie,comments
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token


# Register your models here.
admin.site.register(Token, TokenAdmin)

admin.site.register(insert_movie)

admin.site.register(comments)

