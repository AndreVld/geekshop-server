from django.contrib import admin
from django.contrib.auth.models import Group

from orders.models import Order

admin.site.unregister(Group)


@admin.register(Order)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated', 'status')
    list_filter = ('created', 'user')
    ordering = ('user',)
