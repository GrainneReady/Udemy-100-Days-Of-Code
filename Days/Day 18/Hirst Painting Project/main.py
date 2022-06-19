# This is a program I made following Udemy's Day 18 of 100 Days of Code
#   The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Project Links:
#   https://pypi.org/project/colorgram.py/
#   https://replit.com/@appbrewery/hirstpainting-final (Solution)
# Requirements:
#   Use the 'colorgram' package, a Python library that lets you extract colors from images ✔
#   Print out a list of all the colors extracted from the image where each item in the list is a tuple ✔
#   Paint a painting with 10 x 10 rows of spots
#   Each of the dots should be about 20 in size and be spaced apart by 50 spaces ✔

# import colorgram
# colors = colorgram.extract('Days\Day 18\Hirst Painting Project\image.jpg', 40)


# def RGB_Tuple_List_Generator(colors):
#     rgb_colors = []
#     for color in colors:
#         new_color = (color.rgb[0], color.rgb[1], color.rgb[2])
#         rgb_colors.append(new_color)
#     return rgb_colors[3:]   # Start from index 3 as indexes 0 to 2 are background colors

# print(RGB_Tuple_List_Generator(colors))
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()

NUMBER_OF_DOTS = 100
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

for y in range(10):
    tim.setposition(-325, -275 + (y * 50))
    for x in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

screen = t.Screen()
screen.exitonclick()
