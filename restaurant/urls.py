from django.urls import path

from .views import RestaurantDrawLotsView

urlpatterns = [
    path('', RestaurantDrawLotsView.as_view(), name='restaurant-drawlots')
]
