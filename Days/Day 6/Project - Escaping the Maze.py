# This program is a direct copy of a program I made following Udemy's Day 6 of 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#   https://www.udemy.com/course/100-days-of-code/
# Challenge Link:
#   https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Instructions:
#   Reeborg was exploring a dark maze and the battery in its flashlight ran out.
#   Write a program using an if/elif/else statement so Reeborg can find the exit. 
#   The secret is to have Reeborg follow along the right edge of the maze, turning right if it can,
#   going straight ahead if it can’t turn right, or turning left as a last resort.
# Goal to Achieve:
#   The final position of the robot must be (x, y) = (6, 4)
# What you need to know:
#   The functions move() and turn_left().
#   Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#   How to use a while loop and if/elif/else statements.
#   It might be useful to know how to use the negation of a test (not in Python).


#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#def jump_hurdle():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()
#
#while not at_goal():
#    if right_is_clear():
#        turn_right()
#        move()
#    elif not right_is_clear() and front_is_clear():
#        move()
#    else:
#        turn_left()