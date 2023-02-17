from django.contrib import admin
from webapp.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    fields = ['name', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'price']
    list_filter = ['name', 'category', 'price', 'created_at']
    search_fields = ['name', 'category', 'price', 'created_at']
    fields = ['name', 'description', 'category', 'price', 'created_at', 'updated_at', 'image']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
