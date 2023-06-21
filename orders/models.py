from django.db import models

# Create your models here.
class Orders(models.Model):
    order_status = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8,decimal_places=2)
    order_item = models.JSONField()

def isExist(self):
    if Orders.objects.filter(order_item =self.order_item):
        return True
    return False
