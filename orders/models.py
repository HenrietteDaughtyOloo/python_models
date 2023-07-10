from django.db import models
# from django.contrib.auth.models import 
from my_cart.models import MyCart
from customer.models import Customer
from delivery.models import Delivery

# Create your models here.
class Orders(models.Model):

    
    order_status = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8,decimal_places=2)
    order_item = models.JSONField()
    cart_relations = models.OneToOneField(MyCart, null=True, on_delete=models.CASCADE)
    customer_relations = models.ForeignKey(Customer, null=True,on_delete=models.CASCADE)
    delivery_relations = models.OneToOneField(Delivery, null=True,on_delete=models.CASCADE )

def isExist(self):
    if Orders.objects.filter(order_item =self.order_item):
        return True
    return False
