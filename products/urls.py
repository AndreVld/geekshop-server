from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ProductsView

app_name = 'products'

urlpatterns = [
    path('', cache_page(60)(ProductsView.as_view()), name='index'),
    path('<int:category_id>/', cache_page(60)(ProductsView.as_view()), name='product'),
    path('page/<int:page>/', cache_page(60)(ProductsView.as_view()), name='page'),
]
