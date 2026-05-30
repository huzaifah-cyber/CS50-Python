names = []

while True:
    try:
        name = input("Name: ").title()
        names.append(name)

    except EOFError:
        print()
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif len(names) > 2:
    print(f"Adieu, adieu, to {', '.join(names[0:-1])}, and {names[-1]}")
else:
    print("Goodbye to no one!")
