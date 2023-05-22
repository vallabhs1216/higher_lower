# Input for results
guess = input("Enter win or lose")

#
secret_num = 12
guesses_allowed = 5
guesses_left = 100
guesses_left -= 1
max_guess = 1
rounds_played = 0
rounds_played += 1

# score list
rounds_won = 0
rounds_lost = 0
scores = []

#  Checks if guess is or isn't secret number
while guess != secret_num:
    if guess == secret_num:
        # If first guess is secret number or if guess is secret number respond
        if guesses_left == guesses_allowed - 1:
            print("Congratulations you got it on your first guess!")
            rounds_won += 1
        else:
            print("Well done you got the secret number correct")
            rounds_won += 1
            break

    if guess != secret_num:
        print("Sorry you didn't get it in the amount of guesses given.")
        print(f"The number was {secret_num}")
        rounds_lost += 1
        break

guesses_taken = max_guess - guesses_allowed
scores.append(guesses_taken)
print()

if rounds_played >= 1:
    scores.sort()
    best_score = scores[0]
    worst_score = scores[-1]
    average = sum(scores) / len(scores)

    win_percent = rounds_won / rounds_played * 100
    lose_percent = rounds_lost / rounds_played * 100

    print()
    print(win_percent)
    print(lose_percent)
    print()
    print(best_score)
    print(worst_score)
    print(average)
    print()