from django.contrib import admin
from django.db import models
from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey('catalog.Item', on_delete=models.CASCADE, related_name='+')
    amount = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.cartitem.price * self.amount


class Order(models.Model):
    shipping = models.TextField(default='')


