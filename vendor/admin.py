from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "vendor_number", "vendor_address","vendor_rating","vendor_paid_status")
admin.site.register(Vendor,VendorAdmin)