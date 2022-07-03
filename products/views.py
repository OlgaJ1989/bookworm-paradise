""" File specyfying what views can be found in the app. """
from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    """ A view generating the books, their sorting, and search queries """
    books = Book.objects.all()
    context = {'books': books, }
    return render(request, 'products/books.html', context)


def book_details(request, book_id):
    """ A view generating each book's details """
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book, }
    return render(request, 'products/book_details.html', context)
