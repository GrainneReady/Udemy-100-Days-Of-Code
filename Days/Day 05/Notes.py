# Section 5 - For Loops, Range and Code Blocks

# For Loop
# for item in list_of_items:
#   Do Something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    #print(fruit + " Pie")
print(fruits)

# range(min, max[non inclusive], step)
sumOfNumbers = 0
for number in range(1, 101): # Max in range is non inclusive
    sumOfNumbers += number
print(sumOfNumbers)