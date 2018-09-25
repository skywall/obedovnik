from slack import SlackBot
from parser import parse_restaurants

restaurants = parse_restaurants().sort()
bot = SlackBot()

for r in restaurants:
    # print(r.post_daily_menu_to_slack(bot))
    print(r)

## send poll
max = 10
for i in range(0, len(restaurants), max):
    bot.send_poll("Poll title", restaurants[i:i + max])

