from django.shortcuts import render, redirect
from . models import Books
from . forms import BookForm

# Create your views here.

def display_books(request):
    books = Books.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'books/books.html', context)

def add_book(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm()
    
    context = {
        "form": book_form,
    }
    return render(request, 'books/book_form.html', context)


def edit_book(request, id):
    specific_book = Books.objects.get(id=id)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=specific_book)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(instance=specific_book)
    
    context = {
        "form": book_form,
    }
    return render(request, 'books/book_form.html', context)

def delete_book(request, id):
    specific_book = Books.objects.get(id=id)
    specific_book.delete()
    return redirect("/")
