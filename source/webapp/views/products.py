from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, Category


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'home.html', context={
        'products': products
    })


def product_view(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def product_add_view(request: WSGIRequest):
    product = Product.objects.all()
    if request.method == 'GET':
        return render(request, 'product_add_view.html', context={
            'product': product,
            'categories': Category.objects.all()
        })
    context = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'category': request.POST.get('category')
    }
    Product.objects.create(**context)
    return redirect('product_view', pk=product.pk)


def product_edit_view(request: WSGIRequest, pk: int):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'product_edit_view.html', context={
            'product': product,
            'categories': Category.objects.all()
        })
    context = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'image': request.POST.get('image'),
        'category': request.POST.get('category'),
        'price': request.POST.get('price')
    }
    Product.objects.filter(pk=pk).update(**context)
    return redirect('product_view', pk=product.pk)


def product_delete(request: WSGIRequest, pk: int):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('products_view')
