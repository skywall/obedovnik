# -*- coding: utf-8 -*-
class Restaurant:
    pass

class RestaurantEmpty(Restaurant):
    def __init__(self, title):
        self.title = title

class RestaurantURL(Restaurant):
    def __init__(self, title, url):
        self.title = title
        self.url = url

class RestaurantZomato(Restaurant):
    def __init__(self, title, zomatoId):
        self.title = title
        self.zomatoId = zomatoId

class RestaurantXPath(Restaurant):
    def __init__(self, title, xPath):
        self.title = title
        self.xPath = xPath
    
