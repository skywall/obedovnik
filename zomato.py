import requests
import ast
import os
from dish import Dish

config = {
    "user_key": os.environ["ZOMATO_USER_KEY"],
    "base_id": "https://developers.zomato.com/api/v2.1"
}


class Zomato():

    def __init__(self):
        self.user_key = config["user_key"]

    def get_daily_menu(self, restaurant_id):
        """
        Zomato daily menu endpoint.
        :param restaurant_id: id of the restaurant
        :return: list of dishes
        """
        self.__is_valid_restaurant_id(restaurant_id)

        headers = {'Accept': 'application/json', 'user-key': config["user_key"]}
        r = requests.get(config["base_id"] + "/dailymenu?res_id=" + str(restaurant_id), headers=headers).content.decode("utf-8")
        a = ast.literal_eval(r)

        if 'code' in a:
            if a['code'] == 404:
                raise ('InvalidRestaurantId')

        a = a['daily_menus'][0]['daily_menu']
        list = []
        for dish in a['dishes']:
            dish = dish['dish']
            list.append(Dish(dish['name'], dish['price']))

        return list


    def __is_valid_restaurant_id(self, restaurant_Id):
        """
        Checks if the Restaurant ID is valid or invalid.
        If invalid, throws a InvalidRestaurantId Exception.
        """
        restaurant_Id = str(restaurant_Id)
        if restaurant_Id.isnumeric() == False:
            raise ValueError('InvalidRestaurantId')

