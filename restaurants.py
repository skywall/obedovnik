from zomato import Zomato
from slack import SlackBot
from slack import SlackBotSettings

class Restaurant:
    pass

class RestaurantEmpty(Restaurant):
    def __init__(self, title, emoji):
        self.title = title
        self.emoji = emoji

    def post_daily_menu_to_slack(self, slack):
        pass # We don't have any information about daily menu       
    
class RestaurantURL(Restaurant):
    def __init__(self, title, emoji, url):
        self.title = title
        self.emoji = emoji
        self.url = url

    def post_daily_menu_to_slack(self, slack):
        formattedUrl = "<" + url + "|" + title + ">"
        slack.sendMessage(formattedUrl)

class RestaurantZomato(Restaurant):
    def __init__(self, title, emoji, zomatoId):
        self.title = title
        self.emoji = emoji
        self.zomatoId = zomatoId

    def post_daily_menu_to_slack(self, slack):
        dishes = Zomato().get_daily_menu(self.zomatoId)
        formattedDishes = self.__formatDailyMenu(dishes)
        print(formattedDishes)
        slack.sendSnippet(self.title, formattedDishes)

    def __formatDailyMenu(self, dishes):
        return "\n".join(str(dish) for dish in dishes)

class RestaurantXPath(Restaurant):
    def __init__(self, title, emoji, xPath):
        self.title = title
        self.emoji = emoji
        self.xPath = xPath

    def post_daily_menu_to_slack(self):
        pass # Not implemented yet

print(RestaurantZomato("", "", 16505875).post_daily_menu_to_slack(SlackBot(SlackBotSettings())))
    
