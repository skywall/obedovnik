from zomato import Zomato

class Restaurant:
    def __str__(self):
        return "{} {}".format(self.emoji, self.title)

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
        formatted_url = "<" + self.url + "|" + self.title + ">"
        slack.send_message(formatted_url)

class RestaurantZomato(Restaurant):
    def __init__(self, title, emoji, zomato_id):
        self.title = title
        self.emoji = emoji
        self.zomatoId = zomato_id

    def post_daily_menu_to_slack(self, slack):
        dishes = Zomato().get_daily_menu(self.zomatoId)
        if dishes:
            formatted_dishes = self.__formatDailyMenu(dishes)
            slack.send_snippet(self.title, formatted_dishes)

    def __formatDailyMenu(self, dishes):
        return "\n".join(str(dish) for dish in dishes)

class RestaurantXPath(Restaurant):
    def __init__(self, title, emoji, xPath):
        self.title = title
        self.emoji = emoji
        self.xPath = xPath

    def post_daily_menu_to_slack(self):
        pass # Not implemented yet
