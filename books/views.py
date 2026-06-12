from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Book, Category


def home(request):

    top10_books = Book.objects.filter(
        is_top10=True
    )[:10]

    featured_books = Book.objects.filter(
        is_featured=True
    )[:10]

    new_arrivals = Book.objects.filter(
        is_new_arrival=True
    ).order_by('-created_at')[:10]

    categories = Category.objects.all()

    return render(
        request,
        'home.html',
        {
            'top10_books': top10_books,
            'featured_books': featured_books,
            'new_arrivals': new_arrivals,
            'categories': categories
        }
    )


def book_list(request):

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    books = Book.objects.all()

    if query:

        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    if category_id:

        books = books.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    return render(
        request,
        'books/book_list.html',
        {
            'books': books,
            'query': query,
            'categories': categories,
            'selected_category': category_id
        }
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