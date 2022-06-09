# Section 9 - Dictionaries and Nesting

# Dictionary {Key: Value}
#   Key         |   Value
#   Bug         | An error in a program that prevents the program from running as expected
#   Function    | A piece of code that you can easily call over and over again
#   Loop        | The action of doing something over and over again

from tracemalloc import start


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieve Item from dictionary
# Dictionaries have elements which are identified by their key
# If we put in a key which does not exist, we will get a KeyError.
print(programming_dictionary["Bug"])

# Add new piece of data programmatically
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Create empty dictionary
empty_dictionary = {}

# Wipe a dictionary
#programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Looping through a dictionary
for key in programming_dictionary:
    print(key)                              # Print key
    print(programming_dictionary[key])      # Print value
    
# Nesting
#{
#    Key: [List],
#    Key2: {Dict},
#}

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#}

# Nesting list in a list
#["A", "B", ["C", "D"]]

# Nesting dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany":  {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3},
}

print(travel_log)

# Nesting a dictionary inside a list
#[{
#    Key: [List],           # index 0
#    Key2: {Dict},
#},
#{
#    Key: Value,            # index 1
#    Key2: Value,
#}]

# Example of Nesting dictionary inside a list
travel_log = [
    {
      "Country": "France", 
      "cities_visited": ["Paris", "Lille", "Dijon"], 
      "total_visits": 12
    },
    {
      "Country": "Germany", 
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits": 3
    },
]
print(travel_log)

