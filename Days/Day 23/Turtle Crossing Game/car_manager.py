from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
CAR_SPAWN_X_COORDINATES = (300, 901)
CAR_SPAWN_Y_COORDINATES = (-250, 251)
CAR_RESPAWN_X_COORDINATES = (300, 501)
CAR_RESPAWN_Y_COORDINATES = (-250, 251)
CAR_SCREEN_EXCEEDANCE = -320
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        """Generates 15 new cars at random coordinates between (300, -250) and (900, 251)
        Gives them a random color from the COLORS list along with setting their size to stretch_wid=1, strench_len=2, outline=1
        Adds all newly generated cars to the self list of cars
        All cars are Turtle objects from turtle
        """
        for car in range(15):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.speed("fastest")
            new_car.turtlesize(stretch_wid=1, stretch_len=2, outline=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(CAR_SPAWN_X_COORDINATES), random.randint(CAR_SPAWN_Y_COORDINATES))
            self.cars.append(new_car)

    def move_cars(self):
        """Moves all cars in self.cars
        If a car has moved offscreen, it will respawn it at a random coordinate between (300, -250) and (500, 251)
        """
        for car in self.cars:
            car.backward(self.cars_speed)
            if car.xcor() < CAR_SCREEN_EXCEEDANCE:
                car.goto(random.randint(CAR_RESPAWN_X_COORDINATES), random.randint(CAR_RESPAWN_Y_COORDINATES))

    def increment_cars_speed(self):
        """Increases the speed that the cars will move at, based on MOVE_INCREMENT
        """
        self.cars_speed += MOVE_INCREMENT

    def collisionCheck(self, player):
        """Checks if a player object has collided with a car object in self.cars.

        Args:
            player (Player): The player object to check if any car has collided with

        Returns:
            bool: True if player has collided with a car
                  False if player has not collided with a car
        """
        for car in self.cars:
            if (car.ycor() - 10 < player.ycor() + 10) and (car.ycor() + 10 > player.ycor() - 10) and (car.xcor() - 20 < player.xcor() + 10) and (car.xcor() + 20 > player.xcor() - 10):
                return True
        return False
