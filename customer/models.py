from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def register(self):
        self.save

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False

class Meta:
    verbose_name_plural = "customer"