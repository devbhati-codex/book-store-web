from django.contrib import admin
from .models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'price',
        'stock',
        'category',
        'is_top10',
        'is_featured'
    ]

    list_filter = [
        'category',
        'is_top10',
        'is_featured'
    ]

    search_fields = [
        'title',
        'author'
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }