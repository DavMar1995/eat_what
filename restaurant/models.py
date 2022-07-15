from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    ratings_total = models.IntegerField(null=True)
    price_level = models.IntegerField(null=True)
