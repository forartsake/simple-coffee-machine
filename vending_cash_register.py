class CashRegister:
    COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_taken = 0

    def show_report(self):
        """Shows the current machine profit"""
        print(f"${self.profit}")

    def money_process(self):
        """ Returns the change after calculating """
        print("Insert your coins")
        for coin in self.COINS:
            self.money_taken += int(input(f"How many {coin} would you like to insert? ")) * self.COINS[coin]
        return self.money_taken

    def process_payment(self, price):
        """If the sum is correct returns True, otherwise False"""

        self.money_process()
        if self.money_taken >= price:
            change = round(self.money_taken - price, 2)
            print(f"Here is your ${change} change")
            self.profit += price
            self.money_taken = 0
            return True
        else:
            print("Please insert correct amount. Coins are returned")
            self.money_taken = 0
            return False
