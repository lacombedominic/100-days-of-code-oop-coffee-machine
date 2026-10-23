import money_machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_running = True

while machine_running:

    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    valid_drink = menu.find_drink(user_choice)

    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        CoffeeMaker().report()
        money_machine.report()
    elif valid_drink:
        if coffee_maker.is_resource_sufficient(valid_drink): # If there are enough resources for the drink (returns true).
            user_money = money_machine.process_coins()
            user_payment = money_machine.make_payment(user_money)
    #     elif not coffee_maker.is_resource_sufficient(user_choice): # If there is not enough resources. Return False.
    #         machine_running = False
    #             # If there is enough money, make the drink and add it to the machine.
    # else:
    #     print("That is an invalid option. Please try again.")