import random
import math


# HL component 1 - Get and Check for user inputs

# Number checking function
def int_check(question, low=None, high=None, exit_code=None):
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
                          f" than or equal to {low}")
                    continue

            return response
        except ValueError:
            print("Please enter an integer")
            continue


# Function for decoration
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


#  Checks how many rounds user wants to play
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


# Checks for a yes or no input for instructions.
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# Shows instructions on how to play
def instructions():
    print("---------------------------")
    print("------ Instructions -------")
    print("---------------------------")
    print()
    print()
    print("Pick a Minimum and Maximum number for the range of the secret number.")
    print("You can then pick how many times you want to play, or press <enter> for infinite rounds.")
    print()
    print("The amount of guess you get will be automatically generated and told to you.")
    print()
    print("The main objective is to guess the randomly generated secret number.")
    print("If your guess is higher or lower than the secret number the program will tell you.")
    print()


# Main Routine starts here
statement_generator("Welcome to Higher Lower", "*")

# Asks user if they have played, prints instructions if user has not.
played_before = yes_no("Have you played the game before? ")

# Prints instructions
if played_before == "no":
    instructions()

# Loops game to ask if user wants to play again
play_again = "yes"
while play_again == "yes":

    # Gets high, low and number of rounds wanted
    lowest = int_check("Low Number: ")
    highest = int_check("High Number: ", lowest + 1)

    # Game scoring
    scores = []
    rounds_won = 0
    rounds_lost = 0

    # Calculate Maximum guesses
    max_guess = (math.log2(highest - lowest + 1)) + 1
    print(f"Max guesses: {max_guess:.0f}")

    # Ask user for # of rounds or <enter> for infinite rounds
    rounds_played = 0
    rounds = check_rounds()

    # Checks if mode is regular and prints short instruction
    start = ""
    mode = "regular"
    choose_instruction = f"Pick a number in between {lowest} and {highest} "

    # Checks if mode is infinite
    if rounds == "":
        mode = "infinite"
        rounds = 5

    while rounds_played < rounds:

        # Rounds Heading - Displays if user has chosen infinite or normal mode
        # Along with how many rounds have been played.
        print()

        if mode == "infinite":
            heading = f"Continuous Mode: Round {rounds_played + 1}"
            rounds += 1
        else:
            heading = f"Round {rounds_played + 1} of " \
                      f"{rounds}"
        print(heading)
        print(f"{choose_instruction} or 'xxx' to end ")

        rounds_played += 1

        guesses_allowed = max_guess

        # Computer chooses random integer from chosen range.
        secret_num = random.randint(lowest, highest + 0)

        # List for already guessed integers
        guess = []
        already_guessed = []
        guesses_left = guesses_allowed
        num_won = 0

        # Checks for if guess is secret number of not and returns response
        while guess != secret_num and guesses_left >= 1:

            # Checks for guess
            guess = int_check("Guess: ", lowest, highest, "xxx")

            # Exit code
            if guess == "xxx":
                rounds_played = rounds
                break
            # Checks for duplicate guess
            if guess in already_guessed:
                print("You already guessed that number! Please try again"
                      f" You still have {guesses_left:.0f} guesses left")
                continue

            guesses_left -= 1
            already_guessed.append(guess)

            # Lets the game carry on if guesses left is more than or equal to 1

            if guesses_left >= 1:

                # If guess is more than on less than secret number return response
                if guess < secret_num:
                    print(f"Too low, try guessing a higher number. \t|\t "
                          f"Guesses left: {guesses_left:.0f}")
                elif guess > secret_num:
                    print("Too high, try guessing a lower number. \t|\t"
                          f"Guesses left: {guesses_left:.0f}")
                else:
                    if guess < secret_num:
                        print("Too low!")
                    elif guess > secret_num:
                        print("Too high!")

        # Checks if guess is or isn't secret number and returns response
        # Checks if round is won or lost for end game stats
        if guess == secret_num:
            # If first guess is secret number or if guess is secret number respond
            if guesses_left == guesses_allowed - 1:
                print("Congratulations you got it on your first guess!")
                rounds_won += 1

            else:
                print("Well done you got the secret number correct")
                rounds_won += 1

        if guess != secret_num:
            print("Sorry you didn't get it in the amount of guesses given.")
            print(f"The secret number was {secret_num}")
            rounds_lost += 1

        # Gets guesses taken
        guesses_taken = max_guess - guesses_left
        scores.append(guesses_taken)

    # Calculates best worst and average score
    scores.sort()
    best_score = scores[0]
    worst_score = scores[-1]
    average = sum(scores) / len(scores)

    # When game ends calculates win and lose percentage and shows game stats
    if rounds_played >= 1:
        win_percent = rounds_won / rounds_played * 100
        lose_percent = rounds_lost / rounds_played * 100

        print()
        statement_generator(f"Best Score: {best_score:.0f} | Worst Score: {worst_score:.0f} | Average: {average:.0f}", "=")
        print()
        statement_generator(f"Win percent: {win_percent:.0f}% | Lose percent: {lose_percent:.0f}%", "=")
        print()

    play_again = yes_no("Would you like to play again? ")

if play_again == "no":
    print("Thanks for playing")
