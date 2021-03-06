from django.db import models



class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2) #max_dig - всего сколько, decimal - кол-во после запятой
    count = models.PositiveIntegerField()

class ItemAmount(models.Model):
    class Meta:
        abstract = True
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='+')
    amount = models.PositiveIntegerField()
