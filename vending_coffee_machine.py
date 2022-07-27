class VendingCoffeeMachine:

    def __init__(self):
        self._resources = {
            "water": 5000,
            "milk": 2000,
            "coffee": 1000
        }

    def current_resources(self):
        """Shows available resources for making coffee"""
        print(f"Current resources:\nWater: {self._resources['water']} ml.\nMilk: {self._resources['milk']} ml."
              f"\nCoffee: {self._resources['coffee']} g. ")


    def is_resources_enough(self, order):
        """In case when the drink can be made returns True, otherwise False"""
        is_enough = True

        for item in order.ingredients:
            if order.ingredients[item] > self._resources[item]:
                is_enough = False
                print(f"Sorry we run out of {item}")

        return is_enough


    def make_order(self, order):
        """Reduces resources by a specific amount of ingredients and fulfills the order"""
        for item in order.ingredients:
            self._resources[item] -= order.ingredients[item]
        print(f"Please take your {order.drink}. Thank you!")
