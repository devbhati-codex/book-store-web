from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Order(models.Model):

    PAYMENT_METHODS = (
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
        ('COD', 'Cash On Delivery'),
    )

    PAYMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )

    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    order_number = models.CharField(
        max_length=20,
        unique=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Shipping Details
    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=10
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=6
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS
    )

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default='PENDING'
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price_at_time = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.book.title} ({self.quantity})"