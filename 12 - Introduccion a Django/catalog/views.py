from django.shortcuts import render
from .models import BookInstance, Book,Author, Gender


def index(request):
    num_books = Book.objects.all().count() #Del modelo book obtiene todos los objetos y los cuenta
    num_booksInstances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    book_available = BookInstance.objects.filter(status__exact = 'a').count()

    return render(
        request,
        'index.html', #templates
        context = {
            'num_books': num_books,
            'num_booksInstances': num_booksInstances,
            'num_authors': num_authors,
            'book_available': book_available,
        }
    )