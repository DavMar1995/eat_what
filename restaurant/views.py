from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Restaurant
import json

# Create your views here.

GOOGLE_MAP_RESTAURANTS_FILES = [
    'restaurant_1.json',
    'restaurant_2.json',
    'restaurant_3.json',
]


def read_data(files=GOOGLE_MAP_RESTAURANTS_FILES):
    restaurant_list = []

    for file in files:
        with open(file, 'r') as f:
            restaurants = json.load(f)

            for restaurant in restaurants['results']:
                rest = Restaurant(
                    name=restaurant['name'],
                    rating=restaurant['rating'],
                    vicinity=restaurant['vicinity'],
                    price_level=restaurant['price_level'] if 'price_level' in restaurant else -1,
                    user_ratings_total=restaurant['user_ratings_total'])

                print(rest)
                rest.save()

                # restaurant_list.append({
                #     'name': restaurant['name'],
                #     'rating': restaurant['rating'],
                #     'vicinity': restaurant['vicinity'],
                #     'price_level': restaurant['price_level'] if 'price_level' in restaurant else -1,
                #     'user_ratings_total': restaurant['user_ratings_total'],
                # })
    # print(restaurant_list)


class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 100

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
