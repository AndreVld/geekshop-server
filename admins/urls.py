from django.urls import path

from admins.views import index, UsersListView, UsersCreateView, UsersUpdateView, UserDeleteView, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UsersListView.as_view(), name='admin_users'),
    path('users/create/', UsersCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>', UsersUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>', UserDeleteView.as_view(), name='admin_users_remove'),
    path('category/read/', CategoryListView.as_view(), name='admin_category_read'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category/remove/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_remove'),
]
