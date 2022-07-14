from re import A
from django.contrib import admin

from .models import Author, Gender, Book, BookInstance

admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Book)
admin.site.register(BookInstance)
