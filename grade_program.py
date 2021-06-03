#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 3, 2021
# This program asks the user to input a level and converts it to its middle
# percentage using a function that returns the percentage

def calc_mark(level):
    # converts the level inputted to the middle percentage and returns it
    # if the input is invalid, the function returns -1
    if (level == "4+"):
        percentage = 98
    elif (level == "4"):
        percentage = 91
    elif (level == "4-"):
        percentage = 83
    elif (level == "3+"):
        percentage = 78
    elif (level == "3"):
        percentage = 75
    elif (level == "3-"):
        percentage = 71
    elif (level == "2+"):
        percentage = 68
    elif (level == "2"):
        percentage = 65
    elif (level == "2-"):
        percentage = 61
    elif (level == "1+"):
        percentage = 58
    elif (level == "1"):
        percentage = 55
    elif (level == "1-"):
        percentage = 51
    elif (level == "R"):
        percentage = 25
    else:
        percentage = -1
    return percentage


def main():
    while True:
        # ask the user to input a level
        level_string = input("Enter the level you want to convert to\
 percentage: ")
        # convert to the middle percentage using the calc_mark() function
        level_int = calc_mark(level_string)

        if (level_int == -1):
            # check if the input is invalid and display an error message
            print()
            print("{} is not a valid level.". format(level_string))
            print()
        else:
            # display the level converted to the middle percentage
            print()
            print("{0} has a middle percentage of {1}%.\
". format(level_string, level_int))
            break


if __name__ == "__main__":
    main()
