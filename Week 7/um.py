import re


def main():
    print(count(input("Text: ")))


def count(s):
    if findings := re.findall(r"\Wum\W| um\W|^um,|,um\s?|^um\W$|^um\W?|^um$", s, re.I):
        return len(findings)
    else:
        return 0
# Alternate AHHHHHHHHHHHHHH
# def count(s):
#     # \b matches the start AND end of the word automatically
#     findings = re.findall(r"\bum\b", s, re.IGNORECASE)
#     return len(findings)

if __name__ == "__main__":
    main()