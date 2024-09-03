from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    amount = models.IntegerField()
    unit_price = models.IntegerField()


    def __str__(self) -> str:
        return str(self.product)
