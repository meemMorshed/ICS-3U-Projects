"""
    Author: Meem Morshed

    Date: October 4, 2020

    Description: This program prompts the user to enter the three constants
    for their quadratic equation, and then calculates and displays
    the two roots for that quadratic equation, rounded to two
    decimal places.
"""

def main():

    """This function defines the main program logic. Prompts user for input and
    stores them as a, b, c."""

    a = float(input("What is the first constant of your quadratic equation?: "))
    b = float(input("What is the second constant of your quadratic equation?: "))
    c = float(input("What is the third constant of your quadratic equation?: "))

    formula(a, b, c)

def formula(a, b, c):

    """This function takes a, b, c and performs calculations to get the two roots.
    This function calls the display_result function when done."""

    root1 = (b ** 2 - 4 * a * c) ** 0.5
    root1 = (-b + root1) / (2 * a)

    root2 = (b ** 2 - 4 * a * c) ** 0.5
    root2 = (-b - root2) / (2 * a)

    display_result(root1, root2)


def display_result(root1, root2):

    """This function takes the two roots, rounds them to two decimal places, and
    displays it."""

    # This will round roots if they are complex numbers
    rounded1 = round(root1.real, 2) + (round(root1.imag, 2) * 1j or 0)
    rounded2 = round(root2.real, 2) + (round(root2.imag, 2) * 1j or 0)

    # Rounds roots and displays them
    print("The two roots for your quadratic formula are", rounded1, "and", rounded2)

main()
