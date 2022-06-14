# This program is a direct copy of a program I made following Udemy's Day 15 of 100 Days of Code
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/coffee-machine-start
#   https://replit.com/@appbrewery/coffee-machine-final (Solution)
# Notes:
#   The machine starts off with 300ml water, 200ml milk, and 100g coffee
# Instructions:
#   Make a coffee machine
#   1. Makes 3 Hot flavours (Espresso, Latte, Cappucino)
#       Espresso: 50ml Water, 18g Coffee $1.50
#       Latte: 200ml Water, 24g Coffee, 150ml Milk $2.50
#       Cappucino: 250ml Water, 240g Coffee, 100ml Milk $3.00
#   2. Coin Operated using American Coins
#       Penny => 1 cent | Nickel => 5 cents | Dime => 10 cents | Quarter => 25 Cents
# Requirements:
#   Print Report - Need to know how much resources are left
#   Check resources sufficient?
#   Process Coins
#   Check Transaction is successful
#   Make coffee and deduct resources

CENTS_IN_A_QUARTER = 0.25
CENTS_IN_A_DIME = 0.10
CENTS_IN_A_NICKEL = 0.05
CENTS_IN_A_PENNY = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

resources_measures = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"
}


def sufficient_resources_checker(drink, resources):
    """Checks to see if there are sufficient resources to make a given drink.

    Args:
        drink (Dictionary): The dictionary of the drink that we have to make sure we have enough resources for
        resources (dict): The current resources

    Returns:
        list: Returns a list of resources that there is not enough of to make the drink. Will return empty list if there are enough resources
    """
    insufficient_resources = []
    ingredients = drink["ingredients"]
    for key in ingredients:
        if resources[key] < ingredients[key]:
            insufficient_resources.append(key)
    return insufficient_resources


def report_checker(resources):
    """ Generates a report of the current resources available along with the amount of each resource.
    Args:
        resources (dict): The current resources

    Returns:
        String: Returns a formatted string of the generated report
    """

    return f"""
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${resources['money']}
"""


def price_checker(drink):
    """Checks the price of the given drink

    Args:
        drink (dict): The drink to check the price of

    Returns:
        float: The cost of the drink
    """
    return drink["cost"]


def coins_sorter(drink):
    """Requests the amount of each type of coin the user is providing, compares it to the price
    of the drink they want to purchase and returns the amount of change they should receive.
    If they do not give sufficient enough coins, -1 will be returned instead for Error Handling purposes.

    Args:
        drink (Dict): The drink to check the price of

    Returns:
        float: The amount of change to be given had they presented a sufficient amount of coins, or -1 if they failed to do so for error handling purposes.
    """
    total = 0
    total += int(input("how many quarters?: ")) * CENTS_IN_A_QUARTER
    total += int(input("how many dimes?: ")) * CENTS_IN_A_DIME
    total += int(input("how many nickels?: ")) * CENTS_IN_A_NICKEL
    total += int(input("how many pennies?: ")) * CENTS_IN_A_PENNY
    price = price_checker(drink)
    if total >= price:
        return round(total - price, 2)
    return -1


def resources_updater(drink, change):
    """Updates the resources by removing what was used to make a drink and adding the money gained from the transaction.

    Args:
        drink (Dict): The drink that was just made that we need to remove resources for
        change (float): The price of the drink that was just purchased
    """
    drink_ingredients = drink["ingredients"]
    for key in drink_ingredients:
        new_resources = resources[key] - drink_ingredients[key]
        resources[key] = new_resources


def menu_drinks_formatter():
    """Formats the names of the drinks on the menu in respect to the format 'name_1/name_2/.../name_n'

    Returns:
        String: returns the names of drinks in the format 'name_1/name_2/.../name_n'
    """
    drinks = ""
    for key in MENU:
        drinks = drinks + key + "/"
    drinks = drinks[:-1]
    return drinks


def coffee_machine():
    """Our coffee machine!
    Will ask a user what drinks they choose, and then follows through with asking how many coins they want to insert, calculates how much change they should receive,
    'makes' the drink, removes the resources used from resources, adds the money gained from the transaction to resources, until the user eventually turns the machine off by
    entering 'off' when asked what they want to drink.
    The user can also ask for a report when asked what they want to drink.
    This report will show what resources are currently in the machine, including the amount of water, milk, coffee, and money.
    """
    off = False
    drink_names = menu_drinks_formatter()
    while not off:
        request = input(f"  What would you like? ({drink_names}): ")
        if request == "report":
            print(report_checker(resources=resources))
        elif request == "off":
            off = True
            return
        elif request in MENU:
            drink_to_make = MENU[request]
            insufficient_resources = sufficient_resources_checker(drink=drink_to_make, resources=resources)
            if not insufficient_resources:
                print("Please insert coins.")
                change = coins_sorter(drink=drink_to_make)
                if change == -1:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["money"] = resources["money"] + drink_to_make["cost"]
                    print(f"Here is your ${change} in change.")
                    resources_updater(drink=drink_to_make, change=change)
                    print(f"Here is your {request} ☕️. Enjoy!")
            else:
                print(f"  Sorry there is not enough {insufficient_resources[0]}.")


coffee_machine()
