import sys

def file_name_checker(name):
    name = name.strip().split(".")
    # if length of file[] is not 2 exit (that is file.csv) or it doesn't end with csv or file name is "" then exit too.
    if not len(name) == 2 or not name[1] == "csv" or name[0] == "":
        sys.exit("Not a CSV file")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    file_name_checker(sys.argv[1])
    file_name_checker(sys.argv[2])

    before = sys.argv[1]
    after = sys.argv[2]
    try:
        with open(before, "r") as b_file,open(after ,"w") as a_file:
            b_file = b_file.readlines()
            a_file.write("first,last,house\n")
            for line in b_file:
                if line == (b_file[0]):
                    continue
                row = line.replace("\"","").split(",")
                # lstrip on row [1] beacuse of " Hannah" refer to csv
                a_file.write(",".join([row[1].lstrip(),row[0],row[2]]))

    except FileNotFoundError:
        sys.exit("Could not read",before)

