from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=32)
    vendor_number = models.CharField(max_length=32)
    vendor_address = models.CharField(max_length=32)
    vendor_rating = models.IntegerField()
    vendor_paid_status = models.BooleanField()


class Meta:
    verbose_name_plural="vendor"
