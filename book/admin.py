from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BooksAuthor)
admin.site.register(BooksBook)
admin.site.register(BooksBookAuthors)
admin.site.register(BooksBookBookshelves)
admin.site.register(BooksBookLanguages)
admin.site.register(BooksBookSubjects)
admin.site.register(BooksBookshelf)
admin.site.register(BooksFormat)
admin.site.register(BooksLanguage)
admin.site.register(BooksSubject)
