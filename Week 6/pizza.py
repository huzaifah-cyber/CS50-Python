import csv
import sys
import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    name = sys.argv[1].strip().split(".")
    #if length of name of file is not 2 exit (that is name.csv) or it doesn't end with csv or is file name is "" then exit too.
    if not len(name) == 2 or not name[1] == "csv" or name[0] == "" :
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate.tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")