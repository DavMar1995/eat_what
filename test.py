import os 
import json
from restaurant.models import Restaurant



GOOGLE_MAP_RESTAURANTS_FILES = [
    'data/restaurant_1.json',
    'data/restaurant_2.json',
    'data/restaurant_3.json',
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
                # restaurant_list.append({
                #     'name': restaurant['name'],
                #     'rating': restaurant['rating'],
                #     'vicinity': restaurant['vicinity'],
                #     'price_level': restaurant['price_level'] if 'price_level' in restaurant else -1,
                #     'user_ratings_total': restaurant['user_ratings_total'],
                # })

    # print(restaurant_list)
    return restaurant_list


def insert_data(data):
    for restaurant in data:
        rest = Restaurant(
            name=restaurant['name'],
            rating=restaurant['rating'],
            vicinity=restaurant['vicinity'],
            price_level=restaurant['price_level'],
            user_ratings_total=restaurant['user_ratings_total'])
        print(rest)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eat_what.settings')
read_data()
# insert_data(read_data())
