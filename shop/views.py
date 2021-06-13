from django.shortcuts import render
from .models import *

def catalog(request):
    return render(request, 'main/catalog/products.html')

def cart(request):
    return render(request, 'main/cart/cart.html')

def sign_in(request):
    return render(request, 'main/auth/sign_in.html')

def sign_up(request):
    return render(request, 'main/auth/sign_up.html')
