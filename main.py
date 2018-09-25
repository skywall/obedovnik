from zomato import Zomato

zomato = Zomato()
for id in [16505875, 17807429, 16506578, 17807425, 18335377, 18335377, 16506939, 18126190, 16506673]:
    restaurant = zomato.get_daily_menu(id)
    print(", ".join(str(x) for x in restaurant))
