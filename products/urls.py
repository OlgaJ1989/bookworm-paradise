from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<book_id>', views.book_details, name='book_details'),
    path('update-review/<str:pk>/', views.update_review, name='update-review'),
]
