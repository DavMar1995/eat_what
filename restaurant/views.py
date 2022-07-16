from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.db.models import Max
from .models import Restaurant
import json
import random

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


class RestaurantDrawLotsView(View):
    template_file = 'restaurant/restaurant_list.html'

    def get(self, request, **kwargs):
        restaurant_list = Restaurant.objects.all()
        result = get_random()
        return render(
            request, self.template_file,
            {
                'restaurant_list': restaurant_list,
                'result': result
            }
        )


def get_random():
    max_id = Restaurant.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        restaurant = Restaurant.objects.filter(pk=pk).first()
        if restaurant:
            return restaurant
