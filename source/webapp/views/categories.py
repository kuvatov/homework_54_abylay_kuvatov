from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Category


def category_add_view(request: WSGIRequest):
    category = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'category_add_view.html', context={
            'category': category
        })
    context = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description')
    }
    Category.objects.create(**context)
    return redirect('products_view')


def categories_view(request: WSGIRequest):
    categories = Category.objects.all()
    return render(request, 'categories_view.html', context={
        'categories': categories
    })


def category_edit_view(request: WSGIRequest, pk: int):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        return render(request, 'category_edit_view.html', context={
            'category': category
        })
    context = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description')
    }
    Category.objects.filter(pk=pk).update(**context)
    return redirect('categories_view')


def category_delete(request: WSGIRequest, pk: int):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories_view')
