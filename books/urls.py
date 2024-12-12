from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('', views.book_list, name='book_list'),
    path('search/', views.search_books, name='search_books'),
]
