from django.db import models


# Create your models here.
class MyCart(models.Model):
    product_name = models.CharField(max_length=32)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_avatar = models.ImageField()
    date_added = models.DateTimeField()

class Meta:
    verbose_name_plural = "my_cart"