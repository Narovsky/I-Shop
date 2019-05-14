from django.contrib import admin

# Register your models here.
from shop.catalog.models import Item


@admin.register(Item)
class catalogAdmin(admin.ModelAdmin):
    pass