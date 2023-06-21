from django.contrib import admin

# Register your models here.
from .models import Customer

class Customer_admin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","phonenumber","password")

admin.site.register(Customer,Customer_admin)
