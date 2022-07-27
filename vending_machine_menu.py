class MachineItem:

    def __init__(self, drink, coffee, milk, water, price):
        self.drink = drink
        self.price = price
        self.ingredients = {
            "coffee": coffee,
            "milk": milk,
            "water": water
        }


class Menu:

    def __init__(self):
        self.menu = [
            MachineItem(drink="espresso", coffee=20, milk=0, water=150, price=2.5),
            MachineItem(drink="americano", coffee=10, milk=0, water=200, price=3.0),
            MachineItem(drink="cappuccino", coffee=15, milk=50, water=250, price=3.5),
            MachineItem(drink="coffee", coffee=10, water=200, milk=0, price=2.0),
            MachineItem(drink="latte", coffee=15, water=200, milk=30, price=3.5)
        ]

    def get_menu_item(self):
        """Returns all available drinks in the menu"""
        menu_choice = []
        for item in self.menu:
            menu_choice.append(item.drink)

        return menu_choice

    def find_drink(self, order):
        """Looks thorough the menu, in case the drink is available returns True, otherwise -- None """
        for item in self.menu:
            if item.drink == order:
                return item

        print("We are sorry, but this drink is not currently available")
