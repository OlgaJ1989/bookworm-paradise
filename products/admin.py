""" File specyfying settings for the admin panel. """
from django.contrib import admin
from .models import Book, Genre, Review


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)
