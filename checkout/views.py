from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KgzUoBBe3oUHbWGInaYKXUFDDeT7Uf7IvrAat9iiAlDeIXXTp7oVYbfZ2OmX5bkfW4PTZ9YCeYsA6QFllEX4idC00KZ819FMN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
