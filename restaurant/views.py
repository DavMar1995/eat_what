from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View
from django.db.models import Max
from .models import Restaurant
from .forms import RestaurantCreationForm, RestaurantUpdateForm
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


class RestaurantCreationView(View):
    template_file = 'restaurant/restaurant_creation.html'
    form_class = RestaurantCreationForm
    model = Restaurant

    def get(self, request):
        form = self.form_class()
        return render(
            request, self.template_file,
            {
                'form': form
            })

    def post(self, request, parent_template=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(
            request, self.template_file,
            {
                'form': form,
            })


class RestaurantDetailView(View):
    template_file = 'restaurant/restaurant_detail.html'
    form_class = RestaurantUpdateForm
    model = Restaurant

    def _getModelObj(self, id):
        restaurantObj = get_object_or_404(self.model, id=id)
        return restaurantObj

    def get(self, request, restaurant_id):
        restaurant = self._getModelObj(restaurant_id)
        form = self.form_class(instance=restaurant)
        return render(
            request, self.template_file,
            {
                'form': form,
                'restaurant': restaurant
            })

    def post(self, request, restaurant_id):
        restaurant = self._getModelObj(restaurant_id)
        form = self.form_class(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(
            request, self.template_file,
            {
                'form': form,
                'restaurant': restaurant
            })
