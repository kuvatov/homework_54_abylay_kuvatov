from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category')
    description = models.TextField(max_length=2000, null=True, blank=True, help_text='Enter a description',
                                   verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added date and time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date and time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product')
    description = models.TextField(max_length=2000, null=True, blank=True, help_text='Enter a description',
                                   verbose_name='Description')
    category = models.ForeignKey(to='webapp.Category', on_delete=models.CASCADE, null=False, blank=False,
                                 verbose_name='Category', related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added date and time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date and time')
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/media/uploads/')

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"
