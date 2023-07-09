from django.db import models


# Create your models here.
class Ratings(models.Model):
    title = models.CharField(max_length=32)
    review = models.CharField(max_length=64)
    rating = models.IntegerField()
    date_of_review = models.DateTimeField()
    cumulative_rating = models.IntegerField()

class Meta:
    verbose_name_plural = "ratings"