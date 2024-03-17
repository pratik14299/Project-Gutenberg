from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BooksBook
from .serializers import BooksBookSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class RetrieveBooks(APIView):
    """
    API endpoint to retrieve a list of books with optional filtering and pagination.

    Query Parameters:
        language (str): Filter books by language (comma-separated list).
        author (str): Filter books by author name (case-insensitive).
        title (str): Filter books by title (case-insensitive).

    Returns:
        JSON response containing paginated list of serialized book objects.
    """
    def get(self, request):
        books = BooksBook.objects.all()

    # Apply filters based on query parameters
        language = request.query_params.get('language')
        author = request.query_params.get('author')
        title = request.query_params.get('title')
        subjects = request.query_params.getlist('subject')
        bookshelves = request.query_params.getlist('bookshelf')
        mime_type = request.query_params.get('mime_type')

        if language:
        # Split the languages string into a list
            languages_list = language.split(',')
        # Create a Q object to OR the queries for each language
            language_query = Q()
            for lang in languages_list:
                language_query |= Q(booksbooklanguages__language__code__iexact=lang)
            books = books.filter(language_query)

        if author:
            books = books.filter(booksbookauthors__author__name__icontains=author)

        if title:
            books = books.filter(title__icontains=title)

        if subjects:
            subject_query = Q()
            for subject in subjects:
                subject_query |= Q(booksubject__name__icontains=subject)
            books = books.filter(subject_query)

        if bookshelves:
            bookshelf_query = Q()
            for bookshelf in bookshelves:
                bookshelf_query |= Q(bookshelves_set__name__icontains=bookshelf)
            books = books.filter(bookshelf_query)

        if mime_type:
            books = books.filter(formats__mime_type__icontains=mime_type)

    # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 20  # Adjust as needed
        result_page = paginator.paginate_queryset(books, request)
        serialized_books = BooksBookSerializer(result_page, many=True)

        return paginator.get_paginated_response(serialized_books.data)

