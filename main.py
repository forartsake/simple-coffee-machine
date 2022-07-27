from vending_coffee_machine import VendingCoffeeMachine
from vending_machine_menu import Menu
from vending_cash_register import CashRegister
from logo import logo
from prettytable import PrettyTable

menu = Menu()
coffee_maker = VendingCoffeeMachine()
money_machine = CashRegister()
table_menu = PrettyTable()
table_menu.field_names = menu.get_menu_item()

machine_is_on = True
print(logo)
table_menu.add_row(['☕', '☕', '☕', '☕', '☕'])
print(table_menu)

while machine_is_on:

    user_order = input(f"\nWhat would you like? \n")

    if user_order == "report":
        coffee_maker.current_resources()
        money_machine.show_report()
    elif user_order == "off":
        machine_is_on = False
    elif user_order == "profit":
        money_machine.show_report()
    else:
        user_drink = menu.find_drink(user_order)
        if coffee_maker.is_resources_enough(user_drink) and money_machine.process_payment(user_drink.price):
            coffee_maker.make_order(user_drink)
