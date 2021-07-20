from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductArmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')
    ordering = ('name',)
    search_fields = ('name',)
