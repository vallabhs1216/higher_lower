import math

for item in range(0, 4):

    low = int(input("Low: "))
    high = int(input("High: "))

    guesses = high - low + 1
    max_raw = math.log2(guesses)
    max_upped = math.ceil(max_raw)
    max_guesses= max_upped + 1
    print(f"Max Guesses: {max_guesses}")

    print()
