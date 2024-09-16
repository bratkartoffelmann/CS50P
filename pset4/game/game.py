import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    else:
        if n > 1:
            break
            # exit loop if n is a valid positive integer

level = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess < 0:
            continue

        if guess < level:
            print("Too small!")
        elif guess > level:
            print("Too large!")
        else:
            print("Just right!")
            break