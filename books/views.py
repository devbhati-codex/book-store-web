from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    return HttpResponse("Online Book Store Home")


def book_list(request):

    books = Book.objects.all()

    return render(
        request,
        'books/book_list.html',
        {'books': books}
    )

def book_detail(request, slug):

    book = get_object_or_404(
        Book,
        slug=slug
    )

    return render(
        request,
        'books/book_detail.html',
        {'book': book}
    )