from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<book_id>', views.book_details, name='book_details'),
    path('delete_a_review/<str:pk>/', views.delete_review, name='delete_review'),
]
