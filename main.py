import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = MenuItem()

machine_running = True

while machine_running:

    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    valid_drink = menu.find_drink(user_choice)
    valid_drink_ingredients = menu_item.ingredients(valid_drink)
    valid_drink_cost = menu_item.cost(valid_drink)

    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        CoffeeMaker().report()
        money_machine.report()
    elif valid_drink:
        if coffee_maker.is_resource_sufficient(valid_drink): # If there are enough resources for the drink (returns true).

            user_payment = money_machine.make_payment()
        #    make_order = coffee_maker.make_coffee(valid_drink)
        else: # If there is not enough resources. Return False.
            machine_running = False
    # else:
    #     print("That is an invalid option. Please try again.")