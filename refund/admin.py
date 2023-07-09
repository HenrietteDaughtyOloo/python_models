from django.contrib import admin
from .models import Refund
# Register your models here.

class RefundAdmin(admin.ModelAdmin):
    list_display =("order_item","time_of_refund_request","reason_for_refund","refund_request_status","actual_refund_status")
    
admin.site.register(Refund, RefundAdmin)


