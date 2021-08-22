from cart.forms import CartAddProductForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *


def index(request):
    products_sort = Product.objects.all()[:4]
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        "products_sort" : products_sort,
        "products" : products,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'main/index.html', context)

    
    





