
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - Exists within functions
#def drink_potion():
#  potion_strength = 2
#  print(potion_strength)  # Will equal to 2
  
#drink_potion()
#print(potion_strength)  # Outside of Scope, so will give NameError (not defined)

# Global Scope
player_health = 10 
def game(): 
  def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)  # Will be possible, as player_health has global scope.
    
#print(drink_potion()) # Not possible, as drink potion is now local to game().

# Defining anything like player_health have a space where the variable is valid. This concept is called the Namespace
# The concept applies to anything you name, including functions

# Unlike java, there is NO blockscope in python
# If you create a variable within a function, it is only available within that function

game_level = 3
#def create_enemy():
  
#enemies = ["Skeleton", "Zombie", "Alien"]
#if game_level < 5:
#  if game_level == 3:
#    new_enemy = enemies[0]
#print(new_enemy)  #it doesn't matter how nested this is, it will still print. UNLESS its in a function

#def create_enemy():
#  enemies = ["Skeleton", "Zombie", "Alien"]
#  if game_level < 5:
#    if game_level == 3:
#      new_enemy = enemies[0]
#print(new_enemy)              # This won't print, as new_enemy is only local to the function here.

# Modifying Global Scope

enemies = 1
def increase_enemies():
  global enemies                # In order to modify the global enemies inside a function, we have to explicitly call it. This is bad practice, so try prevent modification of global
  enemies += 1                  #   variables inside functions if possible. It's confusing and often increases the margin of error when it comes to bugs.
                                #     instead, in this situation, it would be wiser to just return the value of enemies + 1, and set the global enemies to the returned enemies.
  print(f"Enemies inside function: {enemies}")
increase_enemies()
print(f"Enemies outside function: {enemies}")

# Example of previous comment:
def increase_enemies_returned():
  print(f"Enemies inside function: {enemies}")
  return enemies + 1
enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global Constants - Case is all capitals with _ for spaces Examples:
PI = 3.1415962
DAYS_IN_DECEMBER = 31
SOUND_A_DOG_MAKES = "Woof"

