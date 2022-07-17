""" File storing views for the checkout app """
import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_PUBLIC_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('books'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    ) 

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KgzUoBBe3oUHbWGInaYKXUFDDeT7Uf7IvrAat9iiAlDeIXXTp7oVYbfZ2OmX5bkfW4PTZ9YCeYsA6QFllEX4idC00KZ819FMN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
