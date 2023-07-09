from django.contrib import admin
from .models import Ratings

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("title", "review","rating","date_of_review","cumulative_rating",)
admin.site.register(Ratings,RatingAdmin)