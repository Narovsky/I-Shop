from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catalog.models import Item

class Items:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
