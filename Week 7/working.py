# In a file called working.py, implement a function called convert that expects a str in any
# of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
# Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space
# before each. Assume that these times are representative of actual times,
# not necessarily 9:00 AM and 5:00 PM specifically.
#
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# GOAL = 9:00 to 17:00

# Hours: 9 AM to 5:00 PM
# ('9', None, 'AM', '5', '00', 'PM')
import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    hours = "[1-9]|1[0-2]"
    minutes = "[0-5][0-9]"
    if match := re.match(fr"^({hours}):?({minutes})? (AM|PM) to ({hours}):?({minutes})? (AM|PM)$", s):
         # match.group(1),match.group(2),match.group(3),match.group(4),match.group(5),match.group(6)
        hour_1 = match.group(1)
        minute_1 = match.group(2)
        meridian_1 = match.group(3)
        hour_2 = match.group(4)
        minute_2 = match.group(5)
        meridian_2 = match.group(6)

        hour_1 = str(f"{int(hour_1):02}")
        if meridian_1 == "AM" and hour_1 == "12":
            hour_1 = "00"
        if meridian_1 == "PM" and not hour_1 == "12":
            hour_1 = str(int(hour_1)+12)

        hour_2 = str(f"{int(hour_2):02}")
        if meridian_2 == "AM" and hour_2 == "12":
            hour_2 = "00"
        if meridian_2 == "PM" and not hour_2 == "12":
            hour_2 = str(int(hour_2)+12)

        if minute_1 is None:
            minute_1 = "00"
        if minute_2 is None:
            minute_2 = "00"

        return f"{hour_1}:{minute_1} to {hour_2}:{minute_2}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()