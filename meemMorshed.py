"""Author: Meem Morshed

    Date: October. 23, 2020

    Description: This program is a text-based game in which
    the user selects rock, paper or scissors and the computer picks
    picks rock, paper or scissors at random. Whichever side has
    the winning selection wins the game.
"""

import gamefunctions
import random

def cpu():

    """This function selects the computers choice at random and returns it"""

    cpu_choice = random.randint(1, 3)

    if cpu_choice == 1:
        cpu_choice = "Rock"
    elif cpu_choice == 2:
        cpu_choice = "Paper"
    else:
        cpu_choice = "Scissors"

    return cpu_choice


def main(computer_choice):

    """This function decides the outcome of the game. cpu_choice is
    passed in as a paramater"""

    user_input = gamefunctions.user_choice()
    print("\nThe computer chose:", computer_choice)

    outcome = 0

    if user_input == computer_choice:

        print("Tie! Play again to decide the winner!\n")
        main(cpu())

    elif user_input == "Rock":
        if computer_choice == "Paper":
            print("\nPaper wraps rock. You Lose!")
            outcome += 1
        else:
            print("\nRock smashes scissors. You Win!")
            outcome += 1


    elif user_input == "Paper":
        if computer_choice == "Scissors":
            print("\nScissors cut paper. You Lose!")
            outcome += 1
        else:
            print("\nPaper wraps rock. You Win!")
            outcome += 1

    elif user_input == "Scissors":
        if computer_choice == "Rock":
            print("\nRock smashes scissors. You Lose!")
            outcome += 1
        else:
            print("\nScissors cuts paper. You Win!")
            outcome += 1

    return outcome

main(cpu())