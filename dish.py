class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + " " + str(self.price)
