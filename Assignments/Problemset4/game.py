import random

while True:
    try:
        Level = int(input("Level: "))
    except ValueError:
        continue
    else:
        break

ans = random.randint(1, Level)

while True:
    Guess = int(input("Guess: "))
    if Guess > ans:
        print("Too Large.!")
    elif Guess < ans:
        print("Too Small.!")
    else:
        print("Just right.!")
        break
