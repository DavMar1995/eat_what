from django.urls import reverse
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    ratings_total = models.IntegerField(null=True, blank=True)
    price_level = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'restaurant_id': self.id})
