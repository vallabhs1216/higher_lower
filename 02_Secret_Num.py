import random
high = 1
low = 100

# Computer chooses random integer from chosen range.
secret_num = random.randint(high, low)
print(secret_num)

guesses_allowed = 9

# List for already guessed integers
already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret_num and guesses_left >= 1:

    # Checks for guess
    guess = int(input("Guess: "))

    guesses_left -= 1
    already_guessed.append(guess)

    # Lets game carry on if guesses left is more than  or equal to 1
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