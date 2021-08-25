from django.urls import path
from products.views import ProductsView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('<int:category_id>/', ProductsView.as_view(), name='product'),
    path('page/<int:page>/', ProductsView.as_view(), name='page'),
]
