# This is a program I made following Udemy's Day 16 of 100 Days of Code
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/oop-coffee-machine-start
#   https://replit.com/@appbrewery/oop-coffee-machine-final (Solution)
# Notes:
#   The machine starts off with 300ml water, 200ml milk, and 100g coffee
# Instructions:
#   Work on the Coffee Machine we previously worked on during Day 15 and update it to have Object-Oriented Programming (OOP)
#   Each of the files in this folder except for Notes, another_module and OOP Coffee Machine were provided by the course
# Requirements:
#   1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
#   2. Turn off the Coffee Machine by entering “off” to the prompt.
#   3. Print report.
#   4. Check resources sufficient?
#   5. Process coins.
#   6. Check transaction successful?
#   7. Make Coffee.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee = CoffeeMaker()
menu = Menu()
MoneyMachine = MoneyMachine()

machine_running = True
while (machine_running):
    menu_names = menu.get_items()
    choice = input(f"What would you like? ({menu_names}): ")
    if choice == "off":
        machine_running = False
    elif choice == "report":
        CoffeeMaker.report(Coffee)
        MoneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if Coffee.is_resource_sufficient(drink) and MoneyMachine.make_payment(cost=drink.cost):
            Coffee.make_coffee(drink)
