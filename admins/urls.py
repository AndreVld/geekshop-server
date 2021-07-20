from django.urls import path

from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_remove, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>', admin_users_remove, name='admin_users_remove'),
    path('category/read/', CategoryListView.as_view(), name='admin_category_read'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category/remove/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_remove'),
]
