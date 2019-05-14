from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import Item

class Item:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

def index(request:HttpRequest) -> HttpResponse:
    itemlist = [
        Item.model.Item(name='', price=0, count=0)
    ]
    itemlist.sort(key=lambda c: c.name)

    return render(request, "index.html", {
        'items': itemlist,
        'sum': sum(c.price for c in itemlist)
    })