import random


while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue

    if level <= 0:
        continue

    level = random.randint(1, level)
    break

while True:

    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess <= 0:
        continue

    if guess > level:
        print("Too large!")
        continue
    elif guess < level:
        print("Too small!")
        continue
    else:
        print("Just right!")
        break
