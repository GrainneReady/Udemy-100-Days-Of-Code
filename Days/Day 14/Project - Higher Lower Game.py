# This program is a direct copy of a program I made following Udemy's Day 13 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/higher-lower-start
#   https://replit.com/@appbrewery/higher-lower-final (Solution)
#   https://higherlowergame.com (Classic)
# Notes:
# 
# Instructions:
#   No typed instructions were given, instead, there was a walkthrough in the lectures.
#   Make a game similar to higherlowergame.com where two accounts are randomly selected and the user's role is to guess who has more followers
#   For each person they guess right, they gain a point. The goal is to get the most points by getting consecutively correct guesses.
#   If the user guesses one incorrectly, the game ends.

from HigherLowerGameArt import logo, vs
from HigherLowerGameData import data
import random
import os
def accountPicker():
    """Will choose two random accounts' dictionaries from a list of type dictionary.
    It is not possible for the same Account to be chosen twice.
    If there is only one dictionary in the list, the function will return a list with -1 at index 0

    Returns:
        list(Dictionary): a list containing the dictionaries of the two randomly chosen accounts, or -1 if the list only contained 1 Account.
    """
    chosenAccounts = [random.choice(list(data))]
    quit = False
    while not quit:
        accountToAdd = random.choice(list(data))
        if accountToAdd not in chosenAccounts: # Will make sure we don't choose the same Account twice.
            chosenAccounts.append(accountToAdd)
            quit = True
        elif len(data) == 1:    # Error Handling, if there's only one Account to choose from, as we can't compare a Account to themself.
            chosenAccounts[0] = -1
            quit = True
    return chosenAccounts

def accountFormatter(account):
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

def compareFollowerCount(accounts):
    """Takes in a list of type dictionary of two accounts and returns which account has a higher follower_count

    Args:
        accounts (list(dictionary)): The list of the two accounts that we wish to compare the following of

    Returns:
        char: The account (A or B) which has the higher follower_count
    """
    accountA = accounts[0]
    accountB = accounts[1]
    if accountA["follower_count"] > accountB["follower_count"]:
        return 'A'
    else: return 'B'
def HigherOrLower():
    """Plays games of HigherOrLower with the user until they eventually lose.
    The game is played by choosing two accounts at random from a list of dictionaries which are of account details, account A and account B, and the user has to guess which account has
    a higher follower count.
    If the user guesses correctly, they gain a point.
    The point of this game is to get the most correct guesses as thus you gain the most points.
    At the end, the user's final score is shown.
    """
    quit = False
    score = 0
    firstTimeInLoop = True
    while not quit:
        print(logo)
        if firstTimeInLoop:
            firstTimeInLoop = False
        else:
            if choice == correctChoice:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                return
        accountsToCompare = accountPicker()
        if accountsToCompare[0] != -1:
            firstAccount = accountsToCompare[0]
            secondAccount = accountsToCompare[1]
            print(f"Compare A: {accountFormatter(firstAccount)}.")
            print(vs)
            print(f"Against B: {accountFormatter(secondAccount)}.")
            choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            os.system('cls')
            correctChoice = compareFollowerCount(accounts=accountsToCompare)
HigherOrLower()