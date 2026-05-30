def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    for ch in s:
        if not ch.isdigit() and not ch.isalpha():
            return False

    # AA06
    if len(s) == 4 and s[2:4].isdigit() and s[-2] == "0":
        return False

    # AA063
    if len(s) == 5:
        if s[2:5].isdigit() and s[-3] == "0":
            return False
        if s[3:5].isdigit() and s[-2] == "0":
            return False

    # AA0635
    if len(s) == 6:
        if s[2:6].isdigit() and s[-4] == "0":
            return False
        if s[3:6].isdigit() and s[-3] == "0":
            return False
        if s[4:6].isdigit() and s[-2] == "0":
            return False

    return True

if __name__ == "__main__":
    main()
