from django.contrib import admin

# Register your models here.
from cart.models import Cart


@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    pass