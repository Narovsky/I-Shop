from django.conf import settings
from django.db import models
from catalog.models import ItemAmount


class CartItem(ItemAmount):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='item')
    item = models.ForeignKey('catalog.Item', on_delete=models.CASCADE, related_name='+')
    amount = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.cartitem.price * self.amount

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('catalog.Item')

    @property
    def total_price(self):
        return sum(cartitem.total_price for cartitem in self.items)
