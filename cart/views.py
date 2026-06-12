from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from books.models import Book
from .models import Cart, CartItem


@login_required
def add_to_cart(request, book_id):

    book = get_object_or_404(
        Book,
        id=book_id
    )

    # Out of Stock Protection
    if book.stock <= 0:

        return redirect(
            'book_detail',
            slug=book.slug
        )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book
    )

    if not created:

        if cart_item.quantity < book.stock:

            cart_item.quantity += 1
            cart_item.save()

    return redirect(
        'book_detail',
        slug=book.slug
    )


@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = cart.items.all()

    total = 0

    for item in cart_items:

        item.subtotal = (
            item.book.price *
            item.quantity
        )

        total += item.subtotal

    return render(
        request,
        'cart/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity < item.book.stock:

        item.quantity += 1
        item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity > 1:

        item.quantity -= 1
        item.save()

    else:

        item.delete()

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect('cart')