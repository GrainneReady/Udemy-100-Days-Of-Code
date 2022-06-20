# Section 8 - Functions with Inputs

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
# Function that allows for input
def greet_with_name(name): # Name is parameter, aka name of data passed in
    print(f"Hello {name}")
    print(f"How do you do, {name}?")
    
#greet_with_name("Gráinne") # Gráinne is argument (value of our parameter name)

# Create function that allows for multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
#greet_with("Gráinne", "Dublin")

# Positional Arguments
def my_function(a, b, c):
    print(f"Do this with {a}")
    print(f"Then do this with {b}")
    print(f"Finally do this with {c}")

#my_function(1, 2, 3)        # a = 1, b = 2, c = 3
#my_function(3, 1, 2)        # a = 3, b = 1, c = 2 Order is IMPORTANT!

# KeyWord Arguments
#my_function(a=1, b=2, c=3)  # When we use KEYWORD ARGUMENTS, the order is not important
#my_function(c=3, a=1, b=2)  # a can be first, b can be first, it doesn't matter

# Challenge: Call greet_with(name, location) function with KeyWord Arguments:
greet_with(name = "Gráinne", location = "Dublin")
    
# Positional Arguments: Order matters, harder to understand, uses less space in lines
# Key Word Arguments: Order doesn't matter, easier to understand, uses more space in lines