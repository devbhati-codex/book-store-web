from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'user',
        'full_name',
        'total_price',
        'payment_status',
        'status',
        'created_at'
    ]

    list_filter = [
        'status',
        'payment_status',
        'payment_method'
    ]

    search_fields = [
        'order_number',
        'full_name',
        'phone'
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'book',
        'quantity',
        'price_at_time'
    ]

    search_fields = [
        'book__title'
    ]