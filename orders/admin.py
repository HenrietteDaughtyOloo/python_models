from django.contrib import admin

# Register your models here.
from .models import Orders

class Orders_admin(admin.ModelAdmin):
    list_display=("order_status", "order_date", "order_total","order_item")
admin.site.register(Orders,Orders_admin)

