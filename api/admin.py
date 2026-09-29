from django.contrib import admin
from .models import Genre, Book

admin.site.register([Genre, Book])
