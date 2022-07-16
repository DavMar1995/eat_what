from django.urls import path

from .views import RestaurantDrawLotsView, RestaurantCreationView

urlpatterns = [
    path('', RestaurantDrawLotsView.as_view(), name='restaurant-drawlots'),
    path('create/', RestaurantCreationView.as_view(), name='restaurant-creation')
]
