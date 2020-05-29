from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/shop/shop.html')


def single(request):
    return render(request, 'pages/shop/shop-single-product.html')


def cart(request):
    return render(request, 'pages/shop/shopping-cart.html')
