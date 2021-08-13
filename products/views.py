from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from common.views import DataMixin
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexView(DataMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'GeekShop'


# def index(request):
#     context = {
#         'title': 'GeekShop',
#     }
#     return render(request, 'products/index.html', context)


class ProductsView(DataMixin, ListView):
    template_name = 'products/products.html'
    model = Product
    paginate_by = 3
    title = 'GeekShop - Каталог'

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


# def products(request, category_id=None, page=1):
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#
#     paginator = Paginator(products, 3)
#
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#
#     context = {
#         'title': 'GeekShop - Каталог',
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'products/products.html', context)
