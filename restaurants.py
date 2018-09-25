# -*- coding: utf-8 -*-
class Restaurant:
    pass

class RestaurantEmpty(Restaurant):
    def __init__(self, title, emoji):
        self.title = title
        self.emoji = emoji

class RestaurantURL(Restaurant):
    def __init__(self, title, emoji, url):
        self.title = title
        self.emoji = emoji
        self.url = url

class RestaurantZomato(Restaurant):
    def __init__(self, title, emoji, zomatoId):
        self.title = title
        self.emoji = emoji
        self.zomatoId = zomatoId

class RestaurantXPath(Restaurant):
    def __init__(self, title, emoji, xPath):
        self.title = title
        self.emoji = emoji
        self.xPath = xPath
    
