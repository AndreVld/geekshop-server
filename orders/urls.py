from django.urls import path

from orders.views import OrderList, order_forming_complete, OrderItemsCreate, OrderReadView, OrderUpdateView, \
    OrderDeleteView, get_product_price

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='order'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderReadView.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', get_product_price),

]
