from django.db import models

# Create your models here.
class Refund(models.Model):
    order_item = models.CharField(max_length=34)
    time_of_refund_request = models.DateTimeField()
    reason_for_refund = models.CharField(max_length=50)
    refund_request_status = models.BooleanField()
    actual_refund_status = models.BooleanField()

class Meta:
    verbose_name_plural = "refund"
