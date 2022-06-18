# Section 17 - Creating Classes
# classes follow PascalCase

# PascalCase (First Letters of words are upper, no spaces, '_', etc.)
# camelCase = (First letter is lower case, but all other first letters of words after that are upper case, no spaces, '_', etc)
# snake_case = (Lower case, '_' for spaces between words)
# class User:
#     pass - To move onto next line of code


# user_1 = User()  # Create new Object from class 'User'
# user_1.id = "001"  # Attach new variable to object
# user_1.username = "angela"  # Attach another new variable to object
# print(user_1.username)  # Show variable is attached

# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"
# You can see that the previous user_1 and user_2 setting of variables was slow and prone to errors, so we can use a Constructor to do this instead:
class User:
    def __init__(self, user_id, username):   # Wasteful to have followers as perameter when they will be initialised to 0 as a default, so remove as a parameter
        self.id = user_id   # initialise attributes
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")  # Creating a new object user_1 and initialising with values "001" and "angela" for user id and username
user_2 = User("002", "jack")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Attributes (can add as many parameters as we wish)
# Class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
#
# my_car = Car(5)   # Initialise my_car with seats = 5


# Adding methods to a class
# things that the object does
# Class Car:
#     def __init__(self, seats):
#         self.seats = seats
#     def enter_race_mode():
#         self.seats = 2
#
# my_car = Car(5)   # Initialise my_car with seats = 5
# my_car.enter_race_mode()  # Call enter_race_mode() method to change seats to 2
