from restaurants import *

list = [RestaurantZomato("Title", ":it::spaghetti:", 17807425), RestaurantURL("Name", "X", "http://www.cattani.cz/")]
SlackBot().send_poll("Poll title", list)
