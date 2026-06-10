from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from cart.models import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout_view(request):

    cart = Cart.objects.get(
        user=request.user
    )

    cart_items = cart.items.all()

    total = 0

    for item in cart_items:
        total += (
            item.book.price *
            item.quantity
        )

    if request.method == 'POST':

        form = CheckoutForm(
            request.POST
        )

        if form.is_valid():

            order = form.save(
                commit=False
            )

            order.user = request.user

            order.total_price = total

            order.order_number = (
                f"ORD{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            order.payment_status = 'SUCCESS'

            order.status = 'CONFIRMED'

            order.save()

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price_at_time=item.book.price
                )

            cart_items.delete()

            return redirect(
                'order_success'
            )

    else:

        form = CheckoutForm()

    return render(
        request,
        'orders/checkout.html',
        {
            'form': form,
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
def order_success_view(request):

    return render(
        request,
        'orders/order_success.html'
    )


@login_required
def my_orders_view(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders
        }
    )