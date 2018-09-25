import json

from restaurants import RestaurantEmpty, RestaurantURL, RestaurantZomato


def parse_restaurants():
    with open("restaurants.json", "r") as myfile:
        data = myfile.read()

    restaurants_list = json.loads(data)["restaurants"]

    result = []

    for restaurant in restaurants_list:
        restaurant_type = restaurant["type"]
        if restaurant_type == "empty":
            parsed = RestaurantEmpty(restaurant["name"], restaurant["emoji"])
        elif restaurant_type == "url":
            parsed = RestaurantURL(restaurant["name"], restaurant["emoji"], restaurant["url"])
        elif restaurant_type == "zomato":
            parsed = RestaurantZomato(restaurant["name"], restaurant["emoji"], restaurant["zomato_id"])
        else:
            parsed = None


        if parsed is not None:
            result.append(parsed)

    return result
