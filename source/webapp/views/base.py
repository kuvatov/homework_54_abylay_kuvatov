from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from webapp.models import Product


def home_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'home.html', context={
        'products': products
    })
