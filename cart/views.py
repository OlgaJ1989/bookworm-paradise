""" File storing the views for the cart app """
from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ A view generating the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view allowing to add a quantity of a specific book to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def modify_cart(request, item_id):
    """ A view allowing to change the quantity \
        of a specific book in the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ A view allowing to delete an item from the cart """
    cart = request.session.get('cart', {})

    del cart[item_id]
    if not cart[item_id]:
        cart.pop(item_id)
    else:
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
