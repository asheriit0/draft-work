from django.contrib import admin
from .models import BasketItem, Order

admin.site.register(BasketItem)

admin.site.register(Order)
