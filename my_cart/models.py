from django.db import models
from inventory.models import Product


# Create your models here.
class MyCart(models.Model):
    product_name = models.CharField(max_length=32)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_avatar = models.ImageField(upload_to='my_cart_images/', null=True)
    date_added = models.DateTimeField()
    products = models.ManyToManyField(Product)

class Meta:
    verbose_name_plural = "MyCart"