from django.urls import path
from . views import display_books, add_book, edit_book, delete_book

urlpatterns = [
   path('', display_books, name='book_list'),
   path('add-book/', add_book, name='add_book'),
   path('edit-book/<int:id>', edit_book, name='edit_book'),
   path('delete-book/<int:id>', delete_book, name='delete_book'),
]