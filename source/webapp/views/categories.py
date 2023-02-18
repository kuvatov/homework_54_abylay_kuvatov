from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

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
