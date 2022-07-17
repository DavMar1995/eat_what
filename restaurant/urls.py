from django.urls import path

from .views import RestaurantDrawLotsView, RestaurantCreationView, RestaurantDetailView

urlpatterns = [
    path('', RestaurantDrawLotsView.as_view(), name='restaurant-drawlots'),
    path('create/', RestaurantCreationView.as_view(), name='restaurant-creation'),
    path('<str:restaurant_id>/', RestaurantDetailView.as_view(),
         name='restaurant-detail')
]
