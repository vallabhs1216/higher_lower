import random


# HL component 1 - Get and Check for user inputs

# Number checking function
def int_check(question, low=None, high=None, exit_code = None):
    situation = ""

    # Checks for situation
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Prints response based on situation
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


# Function for decoration
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine starts here

# Gets high, low and number of rounds wanted

# Ask user for # of rounds or <enter> for infinite rounds


start = ""
mode = "regular"

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1, exit_code="")

# set up rounds / infinite mode
if rounds == "":
    mode = "infinite"
    rounds = 5

guesses_allowed = 5     # change me later!!
# guess = int_check("Guess: ", lowest, highest)

# Computer chooses random integer from chosen range.
secret_num = random.randint(lowest, highest + 1)


# List for already guessed integers
already_guessed = []
guesses_left = guesses_allowed
num_won = 0

# Checks for if guess is secret number of not and returns response
while guess != secret_num and guesses_left >= 1:

    # Checks for guess
    guess = int(input("Guess: "))

    guesses_left -= 1
    already_guessed.append(guess)

    # Lets the game carry on if guesses left is more than  or equal to 1
    if guesses_left >= 1:

        if guess < secret_num:
            print(f"Too low, try guessing a higher number. \t|\t "
                  f"Guesses left: {guesses_left}")
        elif guess > secret_num:
            print("Too high, try guessing a lower number. \t|\t"
                  f"Guesses left: {guesses_left}")
        else:
            if guess < secret_num:
                print("Too low!")
            elif guess > secret_num:
                print("Too high!")
if guess == secret_num:
    if guesses_left == guesses_allowed - 1:
        print("Congratulations you got it on your first guess!")
    else:
        print("Well done you got the secret number correct")
if guesses_left < 1:
    print("Sorry you didn't get it in the amount of guesses given.")


print("Thanks for playing")
