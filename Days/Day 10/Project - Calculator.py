# This program is a direct copy of a program I made following Udemy's Day 10 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Preview Links:
#   https://replit.com/@appbrewery/calculator-start
#   https://replit.com/@appbrewery/calculator-final (Solution)
# Notes:
#   os has a clear function similar to replit
#   Recursion is used in this program
#   If we were to have the operation names in our operation dictionary be set to type str by having quotation marks around them, we would not be able to call our functions (TypeErr)
#   DocStrings can be done using """[info]""" on the first line after a functions' definition. It is good practice to have a description of the function, arguments, and what it returns
#     in said docstring.
# Instructions:
#   No typed instructions were given, instead, there was a walkthrough in the lectures.

import os
from calculatorArt import logo
def Addition(num1, num2):
    """This function will return the sum values of num1 and num2

    Args:
        num1 (float): The first number to add
        num2 (float): The second number to add
    Returns:
    float: Returns the sum of the two numbers
    """
    result = num1 + num2
    return result
def Subtraction(num1, num2):
    """This function will return the result of num1 minus num2 aka num1 - num2

    Args:
        num1 (float): The number we want to minus from
        num2 (float): The number we want to subtract
    Returns:
    float: Returns the result of num1 minus num2
    """
    result = num1 - num2
    return result

def Multiplication(num1, num2):
    """This function will return the result of num1 multiplied by num2 aka num1 * num2

    Args:
        num1 (float): The first number we want to multiply
        num2 (float): The second number we want to multiply
    Returns:
    float: Returns the result of num1 multiplied by num2
    """
    result = num1 * num2
    return result

def Division(num1, num2):
    """This function will return the result of num1 divided by num2 aka num1 / num2

    Args:
        num1 (float): The numerator of the division
        num2 (float): The denominator of the division
    Returns:
    float: Returns the result of num1 / num2
    """
    result = num1 / num2
    return result

operations = {
    "+": Addition,              # Note: CANNOT be in quotes, otherwise will get TypeError when trying to call function
    "-": Subtraction,
    "*": Multiplication, 
    "/": Division
    }

def Calculator():
    """This function will act as a calculator, asking the user for the first Number they want to use in their calculations, then will ask them to choose an operator,
    and then ask for the next number they want to use. Once the operation is done, it will ask the user to type 'y' to continue operations, or 'n' to quit. If
    they enter 'y', the function will continue to run operations on the answer of the previous operation and ask the user for the next number until they eventually type 'n' when asked.

    Args:
        None
    Returns:
        None
    """
    print(logo)
    firstNumber = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    quit = False
    while not quit:
        operation_symbol = input("Pick an operation:")
        nextNumber = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(firstNumber, nextNumber)
        print(f"{firstNumber} {operation_symbol} {nextNumber} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
            firstNumber = answer
        else:
            os.system('cls')
            quit = True
            Calculator()    # Recursion!
            
Calculator()
