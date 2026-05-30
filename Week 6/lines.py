import sys


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    name = sys.argv[1].strip().split(".")
    #if length of name of file is not 2 exit (that is name.py) or it doesn't end with py or is file name is "" then exit too.
    if not len(name) == 2 or not name[1] == "py" or name[0] == "" :
        sys.exit("Not a python file")

    file = sys.argv[1]

    try:
        with open(file) as file:
            count_lines = 0
            for row in file.readlines():
                if row.lstrip().startswith("#") or len(row.strip()) == 0:
                    continue
                else:
                    count_lines += 1

        print(count_lines)

    except FileNotFoundError:
        sys.exit("File does not exist")