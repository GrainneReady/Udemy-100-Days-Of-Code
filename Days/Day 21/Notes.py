# +------------------------------------+
# |             Section 21             |
# +------------------------------------+
# |    Building the Snake Game         |
# |    Inheritance and List Slicing    |
# +------------------------------------+

# Steps for Today (Snake)
#   1. Detect collision with food
#   2. Create a scoreboard
#   3. Detect collision with wall
#   4. Detect collision with tail

# Inheritance
# class Fish(Animal):               # Class fish inherits from animal class
#     def __init__(self) -> None:
#         super().__init__()(self):
#             super().__init__()    # Since we have a superclass (Animal, what we're inheriting from), we need to __init__ the super also.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe()
        print("doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Slicing       [beginning : end + 1 : skip] List and Tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
keys_c_to_e = piano_keys[2:5]
print(keys_c_to_e)

keys_c_to_e_step_2 = piano_keys[2:5:2]  # Skips over every 2nd item
piano_keys_odd_items = piano_keys[::2]  # Gets every 2nd item
reversed_piano_keys = piano_keys[::-1]  # Reverses piano keys, starts from end and goes one by one back to index 0

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
reversed_piano_tuple = piano_tuple[::-1]