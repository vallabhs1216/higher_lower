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

        try:
            response = int(input(question))

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


# Checks for number of rounds
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please enter an integer above 1 or <enter> for infinite rounds"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue

        return response


# Main Routine starts here

# Gets high, low and number of rounds wanted

# Ask user for # of rounds or <enter> for infinite rounds


start = ""
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

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
