def main():
    print(gauge(convert(input("Enter X and Z(X/Z): "))))


def convert(fraction):
    try:
        x, z = fraction.split("/")
        x = int(x)
        z = int(z)

        if z == 0:
            raise ZeroDivisionError
        if x > z:
            raise ValueError
        return round((x / z) * 100)

    except ValueError:
        raise ValueError

def gauge(result):
    if 1 >= result >= 0:
        return "E"
    elif 99 <= result <= 100:
        return "F"
    elif 1 < result < 99:
        return f"{result}%"
    else:
        return "-1%"


if __name__ == "__main__":
    main()