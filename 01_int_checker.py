import random


# HL component 1 - Get and Check for user inputs

# Number checking function
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more"
                          f"than or equal to {low}")
                    continue

            return response
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine

start = ""
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
guesses_allowed = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)

