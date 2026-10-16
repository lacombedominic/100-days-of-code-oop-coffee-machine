from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print report
# Check resources sufficient
# Process coins
# Check transaction successful
# Make coffee

# MenuItem Class - This has the name of the drink, the cost of the drink and the ingredients and amounts required to make the drink.
# Menu Class -

machine_running = True

while machine_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        report = CoffeeMaker().report()
    elif user_choice in Menu().MenuItem():
        if check_resources(resources, user_choice):
            total_money = process_coins()
            enough_money = check_payment(total_money, user_choice, resources)
            if enough_money:
                make_coffee(resources, user_choice)
            else:
                continue
        else:
            continue
    else:
        print("That is an invalid option. Please try again.")