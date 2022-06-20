# NOTE: Like in normal mathematics, Priority of Mathematical Operations in Python will follow the PEMDAS rule
# 1. Parenthesis        ()
# 2. Exponents          **
# 3. Multiplcations     *
# 4. Division           /
# 5. Addition           +
# 6. Subtraction        -
# Steps 3 and 4 are equally as important, likewise for steps 5 and 6.

# Introduction
print("------------------------------------\n Mathematical Operations in Python! \n------------------------------------")

# Addition
add = 5 + 3     # Answer = 8
print("Addition:\n 5 + 3 = " + str(add) + "\n")

# Subtraction
sub = 5 - 3     # Answer = 2
print("Subtraction:\n 5 - 3 = " + str(sub) + "\n")

# Multiplication
mul = 5 * 3     # Answer = 15
print("Multiplication:\n 5 * 3 = " + str(mul) + "\n")

# Division
div = 5 / 3     # Answer = 1.6666666666666667
print("Division:\n 5 / 3 = " + str(div) + "\n")
# NOTE: Division will always result in a float number
#       We can use // instead of / to do floor division
#       The round() function will be of use in division also.

# Modulus
mod = 5 % 3     # Answer = 2 (5 goes into 3 once with a remainder of 2)
print("Modulus:\n 5 % 3 = " + str(mod) + "\n")

# Exponent
exp = 5 ** 3    # Answer = 125
print("Exponent:\n 5^3 = " + str(exp) + "\n")

#   (x += y) is the same as (x = x + y)
#   (x -= y) is the same as (x = x - y)
#   (x *= y) is the same as (x = x * y)
#   (x /= y) is the same as (x = x / y)
#   (x %= y) is the same as (x = x % y)
#   (x **= y) is the same as (x = x ** y)

# An f-string allows us to add various different dataTypes to a string, by adding the variable in curly braces
# Example:
score = 3;
print(f"Your score is {score}")

