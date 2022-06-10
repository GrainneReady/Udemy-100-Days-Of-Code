# Section 10 - Functions with Outputs

def my_function():
    result = 3 * 2
    return result

result = my_function()  # Remember to include '()', otherwise you will just get the function address

# Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        #return                          # Return Void
        return "Invalid Inputs: One or both of the names were empty"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    print("This will never print")

formatted_name = format_name(input("What is your first name? "), input("What is your last name? "))
print(formatted_name)

# DocStrings
# The DocString has to go as the first line after a function's declaration, and has to contain three quotation marks instead of one
# Example:
def format_name_extended(f_name, l_name):
    """Takes in a first name and a last name and returns the names in titlecase

    Args:
        f_name (String): The first name you wish to format into titlecase
        l_name (String): The last name you wish to format into titlecase

    Returns:
        String: Returns the given f_name and l_name in titlecase
    """
    if f_name == "" or l_name == "":
        #return                          # Return Void
        return "Invalid Inputs: One or both of the names were empty"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

    