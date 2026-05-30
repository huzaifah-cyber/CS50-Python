import random


def main():
    level = get_level()
    counter = 0
    total_score = 0
    while counter != 10:
        a = generate_integer(level)
        b = generate_integer(level)
        c = a+b

        for i in range(3):
            try:
                ans = int(input(f"{a} + {b} = "))
            except ValueError:
                print("EEE")
                if i == 2:
                    print(f"{a} + {b} = {c}")
                continue
            if ans == c:
                total_score += 1
                break
            print("EEE")
            if i == 2:
                print(f"{a} + {b} = {c}")

        counter += 1

    print("Score:",total_score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            return level
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
