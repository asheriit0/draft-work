from django.db import models
from dishlist.models import Dishes
from django.contrib.sessions.models import Session


# class BasketItem(models.Model):
#     dishe = models.ForeignKey(Dishes, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     date_added = models.DateTimeField(auto_now_add=True)
#     session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.quantity} x {self.dishe.name}'
#модель корзины
class BasketItem(models.Model):

    dishe = models.ForeignKey(Dishes, on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'basket'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def total_price(self):
        return self.quantity * self.price_per_item

    def __str__(self):
        return f'{self.quantity} x {self.dishe.title} - {self.total_price()} руб.'


#модель заказа
class Order(models.Model):
    items = models.ManyToManyField(BasketItem)
    total_order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        self.total_order_price = sum(item.total_price() for item in self.items.all())
        self.save()