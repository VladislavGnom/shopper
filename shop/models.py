from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField()
    price = models.IntegerField()
    remainder = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category 
