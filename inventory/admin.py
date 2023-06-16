from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created")
    
# Register your models here.
admin.site.register(Product,ProductAdmin)


