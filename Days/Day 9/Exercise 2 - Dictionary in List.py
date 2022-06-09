# This program is a direct copy of a program I made following Udemy's Day 9 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Exercise Link:
#   https://app.codingrooms.com/management/assignments/364955/overview
# Instructions:
#   You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
#   Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#   add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#   You've visited Russia 2 times.
#   You've been to Moscow and Saint Petersburg.
#   DO NOT modify the travel_log directly. You need to create a function that modifies it.
# Submission Result (100%)
#   https://i.gyazo.com/7c2fc903074bd8623086ab4acbf37d81.png

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, number_of_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = number_of_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)