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


def instructions():
    print("---------------------------")
    print("------ Instructions -------")
    print("---------------------------")
    print()
    print()
    print("Pick a Minimum and Maximum number for the range of the secret number.")
    print("You can then pick how many times you want to play or press <enter> for infinite rounds")
    print()
    print("The amount of guess you get will be automatically generated and told to you")
    print()
    print("The main objective is to guess the randomly generated secret number")
    print("If your guess is higher or lower than the secret number the program will tell you")
    print()



    return ""

statement_generator("Welcome to Lucky Unicorn game", "*")
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()
