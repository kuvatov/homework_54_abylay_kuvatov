"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views.categories import category_add_view, categories_view, category_delete, category_edit_view
from webapp.views.products import products_view, product_view, product_add_view, product_delete, product_edit_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", products_view, name='home'),
    path("products", products_view, name='products_view'),
    path("products/add", product_add_view, name='product_add_view'),
    path("products/<int:pk>", product_view, name='product_view'),
    path("products/<int:pk>/edit", product_edit_view, name='product_edit_view'),
    path("products/<int:pk>/delete", product_delete, name='product_delete'),
    path("categories", categories_view, name='categories_view'),
    path("categories/add", category_add_view, name='category_add_view'),
    path("categories/<int:pk>/edit", category_edit_view, name='category_edit_view'),
    path("categories/<int:pk>/delete", category_delete, name='category_delete')
]
