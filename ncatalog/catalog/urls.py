from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('like/<int:book_id>/', like_book, name='like_book'),
    path('comment/<int:book_id>/', comment_book, name='comment_book'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('detail/<int:book_id>/', detail_book, name='detail_book'),
]