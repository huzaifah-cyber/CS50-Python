def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    for ch in word:
        if ch in "aeiou" or ch in "AEIOU":
            word = word.replace(ch, "")
    return word


if __name__ == "__main__":
    main()




