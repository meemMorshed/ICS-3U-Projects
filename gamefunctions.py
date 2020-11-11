"""Author: Meem Morshed

    Date: October. 23, 2020

    Description: This module will display the menu
    for the game and check the choice using input
    validation.
"""

print("A. Rock")
print("B. Paper")
print("C. Scissors \n")

def user_choice():

    """This function prompts the user for input, a, b or c and uses
    input validation. Using the input it converts it into rock, paper,
    or scissors and returns it"""

    user_choice = input("Please enter your choice: ")

    flag = 0

    while flag == 0:

        # Makes sure input is valid
        if len(user_choice) > 1 or len(user_choice) < 1:
            print("\nInvalid choice, please pick again")
            user_choice = input("Please enter your choice: ")

        elif ord(user_choice) >= 97 and ord(user_choice) <= 99:
            flag += 1
        elif ord(user_choice) >= 65 and ord(user_choice) <= 67:
            flag += 1
        else:
            print("\nInvalid choice, please pick again")
            user_choice = input("Please enter your choice: ")

    # Converts input to rock, paper or scissors
    if user_choice == 'a' or user_choice == 'A':
        user_choice = "Rock"
    elif user_choice == 'b' or user_choice == 'B':
        user_choice = "Paper"
    elif user_choice == 'c' or user_choice == 'C':
        user_choice = "Scissors"

    return user_choice