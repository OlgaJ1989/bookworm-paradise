""" File specyfying what views can be found in the app. """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Book, Genre, Review
from .forms import ReviewForm


def all_books(request):
    """ A view generating the books, their sorting, and search queries """
    books = Book.objects.all()
    query = None
    genres = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))
            queries = Q(title__icontains=query) | Q(
                description__icontains=query)
            books = books.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/books.html', context)


def book_details(request, book_id):
    """
    A view generating each book's details and the ReviewForm()
    allowing the user to add a book review
    """

    book = get_object_or_404(Book, pk=book_id)
    reviews = book.reviews.order_by("-posted_on")

    if request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.book = book
                review.save()
                messages.success(request, f'You reviewed {book.title}!')
                return redirect(reverse('book_details', args=[book_id]))
        else:
            form = ReviewForm()

    context = {'book': book, 'reviews': reviews, 'form': form}
    return render(request, 'products/book_details.html', context)


def update_review(request, pk):
    review = get_object_or_404(Review, id=pk)
    form = ReviewForm()
    if request.user == review.author:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review.save()
                messages.success(request, 'Your changes have been saved!')
                return redirect(reverse('book_details', args=[pk]))
    else:
        messages.error(request, 'You are not authorised to edit this review!')
        return redirect(reverse('book_details', args=[pk]))
    context = {'form': form}
    return render(request, 'products/book_details.html', context)
