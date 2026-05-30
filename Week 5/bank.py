def main():
    greet = input("Greeting : ")
    print (f"${value(greet)}")

def value(greet):
    greet = greet.strip().lower()
    if greet[:5] == "hello":
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()