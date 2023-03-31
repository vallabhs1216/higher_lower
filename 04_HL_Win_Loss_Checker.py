# Game history checker from RPS
game_summary = []

rounds_played = 0
rounds_lost = 0
rounds_won = 0

for item in range(0, 5):
    result = input("choose result: ")

    outcome = f"Round {item - 1}: {result}"

    if result == "lost":
        rounds_lost += 1
        rounds_played += 1
    elif result == "won":
        rounds_won += 1
        rounds_played += 1

    # Adds Game result to a list for history
    game_summary.append(f"Round #{rounds_played}: {result}")

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


# Displays history

print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()
print("Thanks for playing")

# Displays game stats with % values to the nearest whole number
print()
print("**** Game Statistics ****")
print(f"Win: {rounds_won}: ({percent_win:.0f}%)\nLoss: {rounds_lost}: ({percent_lose:.0f}%)".format)
print()
