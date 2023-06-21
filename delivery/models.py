from django.db import models

# Create your models here.
class Delivery(models.Model):
    contact_number= models.CharField(max_length=50)
    delivery_date=models.DateTimeField()
    time=models.TimeField()
    cyclist_name = models.CharField(max_length=50)
    delivery_adress = models.CharField(max_length=50)
    status=models.CharField(max_length=50)

