# This program is a direct copy of a program I made following Udemy's Day 13 of 100 Days of Code
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/higher-lower-start
#   https://replit.com/@appbrewery/higher-lower-final (Solution)
#   https://higherlowergame.com (Classic)
# Notes:
#
# Instructions:
#   No typed instructions were given, instead, there was a walkthrough in the lectures.
#   Make a game similar to higherlowergame.com where two accounts are randomly selected and
#   the user's role is to guess who has more followers
#   For each person they guess right, they gain a point.
#   The goal is to get the most points by getting consecutively correct guesses.
#   If the user guesses one incorrectly, the game ends.
import random
import os
from HigherLowerGameArt import logo, vs
from HigherLowerGameData import data


def account_picker():
    """Will choose two random accounts' dictionaries from a list of type dictionary.
    It is not possible for the same Account to be chosen twice.
    If there is only one dictionary in the list, the function will return a list with -1 at index 0

    Returns:
        list(Dictionary): a list containing the dictionaries of the two randomly chosen accounts, 
        or -1 if the list only contained 1 Account.
    """
    accounts_picked = False
    chosen_accounts = [random.choice(list(data))]
    while not accounts_picked:
        account_to_add = random.choice(list(data))
        if account_to_add not in chosen_accounts: # Will make sure we don't choose the same Account
            chosen_accounts.append(account_to_add)
            accounts_picked = True
        elif len(data) == 1:# Error Handling
            chosen_accounts[0] = -1
            accounts_picked = True
    return chosen_accounts


def account_formatter(account):
    """Takes in a dictionary of an account and formats it appropriately for the HigherLower game

    Args:
        account (Dictionary): The account to format

    Returns:
        String: of format '{name}, a {description}, from {country}'
    """
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def compare_follower_count(accounts):
    """Takes in a list of type dictionary of two accounts and returns which account has
    a higher follower_count

    Args:
        accounts (list(dictionary)): The list of the two accounts that we wish to compare

    Returns:
        char: The account (A or B) which has the higher follower_count
    """
    account_a = accounts[0]
    account_b = accounts[1]
    if account_a["follower_count"] > account_b["follower_count"]:
        return 'A'
    return 'B'
def higher_or_lower():
    """Plays games of HigherOrLower with the user until they eventually lose.
    The game is played by choosing two accounts at random from a list of dictionaries which are of
    account details, account A and account B, and the user has to guess which
    account has a higher follower count.
    If the user guesses correctly, they gain a point.
    The point of this game is to get the most correct guesses as thus you gain the most points.
    At the end, the user's final score is shown.
    """
    choice = 'A'
    correct_choice = 'A'
    score = 0
    first_time_in_loop = True
    while not quit:
        print(logo)
        if first_time_in_loop:
            first_time_in_loop = False
        else:
            if choice == correct_choice:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                return
        accounts_to_compare = account_picker()
        if accounts_to_compare[0] != -1:
            first_account = accounts_to_compare[0]
            second_account = accounts_to_compare[1]
            print(f"Compare A: {account_formatter(first_account)}.")
            print(vs)
            print(f"Against B: {account_formatter(second_account)}.")
            choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            os.system('cls')
            correct_choice = compare_follower_count(accounts=accounts_to_compare)          
higher_or_lower()
