from django.contrib import admin

# Register your models here.
from orders.models import OrderItem


@admin.register(OrderItem)
class ordersAdmin(admin.ModelAdmin):
    pass