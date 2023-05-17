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





max_guess = math.log2(highest - lowest + 1)
print(f"Max guesses: {max_guess:.0f}")