""" File specyfying what views can be found in the app. """
from django.shortcuts import render
from .models import Book


def all_books(request):
    """ A view generating the books, their sorting, and search queries """

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)
