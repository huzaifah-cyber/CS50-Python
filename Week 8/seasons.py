import operator
from datetime import date
import re
import sys
import inflect

def main():
    inp = check(input("Date of Birth: "))
    year,month,day = (inp.split("-"))
    year = int(year)
    month = int(month)
    day = int(day)
    today = date.today()
    try:
        birth = date(year,month,day)
        days_list = (str(operator.__sub__(today, birth))).split(" ")
        minutes_passed = (int(days_list[0])*1440)
        p = inflect.engine()
        print(p.number_to_words(minutes_passed,andword="").capitalize()+" minutes")
    except ValueError:
        print("Invalid date")

def check(s):
    if re.match(r"\d\d\d\d-\d\d-\d\d", s):
        return s
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()