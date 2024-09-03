from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField()
    price = models.IntegerField()
    remainder = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    
