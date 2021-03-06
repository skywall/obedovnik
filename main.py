from parser import parse_restaurants
from slack import SlackBot

restaurants = parse_restaurants()
bot = SlackBot()

try:
    ## show menus
    for r in restaurants:
        print(r.post_daily_menu_to_slack(bot))


    ## send poll
    max = 10
    for i in range(0, len(restaurants), max):
        bot.send_poll("Poll", restaurants[i:i + max])
except Exception as exc:
    print(type(exc))
