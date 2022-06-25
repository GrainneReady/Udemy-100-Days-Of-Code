# +-------------------------------------------------------+
# |                        Day 25                         |
# +-------------------------------------------------------+
# | Working with CSV Files and Analysing Data with Pandas |
# +-------------------------------------------------------+

# CSV - Comma Separated Values
#   Each line is a single set of data and each piece of data is separated by ','

# with open("Days\\Day 25\\weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

# import csv

# with open("Days\\Day 25\\weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []   # Challenge: Extract all temperatures from the file and put them into this list ✔
#     for rowIndex in data:
#         if rowIndex[1] != "temp":
#             temperatures.append(int(rowIndex[1]))
#     print(temperatures)

# Pandas Library - A Python Data Analysis Library which is helpful to perform Data Analysis on Tabular data
#   Will need to install this into the projects manually.


import pandas

# Panda takes the first row to be the headers of each column, index 0 will not give you the header, it'll give the first piece of data
# data = pandas.read_csv("Days//Day 25//weather_data.csv")
# Print out as table
# print(data)

# Print row at given index
# print(data.loc[2, :])

# Print row x column (rowIndex=2, col="temp")
# print(data.loc[2, "temp"])

# Print out specific column
# print(data["temp"])
# print(data.temp)

# Print second row and all of ts columns
# print(data.iloc[2,:])

# Print first row and first two columns
# print(data.iloc[0, 0:2])

# Find row that matches request in specific column (Series)
# print(data[data.day == "Monday"])

# DataFrames & Series: Working with Rows & Columns
# print(type(data)) # Is a panda dataframe object
# print(type(data["temp"])) # Is a panda series object
# DataFrame - When theres more than one column (2-dimensional)
# Series - When theres only one column (1-dimensional), like a list

# data_dict = data.to_dict()  # Creates separate dictionary for each of the columns and puts all columns into a dictionary themself. All series are now dictionaries in one big dictionary
# print(data_dict)

# days_list = data["day"].to_list()  # Converts 'day' column (Type Series) into a list (Type List)
# print(days_list)

# Challenge: figure out average temperature in column (Series) of temperatures ✔
# temp_list = data["temp"].to_list()
# average_temp = round(sum(temp_list) / len(temp_list), 2)
# print(f"Average Temperature: {average_temp}")
# The average is also the mean, so we could have done it this way also:
# mean_temp = round(data["temp"].mean(), 2)
# print(f"Mean Temperature: {mean_temp}")

# Challenge: Get maximum value from temperatures column (Series) by using one of the Data Series methods ✔
# maximum_temp = data["temp"].max()
# print(f"Maximum Temperature: {maximum_temp}")

# Challenge: Pull out row from data where temperature was at the maximum
# print(data[data.temp == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)  # Print column's Condition when row day == Monday


# Challenge: Convert Monday's temperature to Fahrenheit ✔

# monday_temp_celsius = int(monday.temp)
# monday_temp_fahrenheit = monday_temp_celsius * 9 / 5 + 32
# print(monday_temp_fahrenheit)

# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("Days\\Day 25\\new_data.csv")

# Create squirrel_count.csv
# Figure out how many squirrels of each primary fur there are
# PRIMARY_FUR_COLOR_INDEX = 8
# squirrel_data = pandas.read_csv("Days\\Day 25\\2018_Central_Park_Squirrel_census_-_Squirrel_Data.csv")
# primary_fur_colors = squirrel_data.iloc[:, PRIMARY_FUR_COLOR_INDEX]
# print(primary_fur_colors.value_counts())
# primary_fur_colors.value_counts().to_csv("Days\\Day 25\\squirrel_count_alt.csv")
# Or Do This:
# grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("Days\\Day 25\\squirrel_count.csv")
