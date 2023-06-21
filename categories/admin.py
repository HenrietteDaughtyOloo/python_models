from django.contrib import admin

# Register your models here.
from .models import Categories
class Categories_admin(admin.ModelAdmin):
    list_display=["category_name"]

admin.site.register(Categories,Categories_admin)
