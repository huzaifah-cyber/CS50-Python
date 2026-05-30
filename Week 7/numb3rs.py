import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    raw = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    if re.search(fr"^({raw}\.){{3}}{raw}$",ip.strip()):
        return True
    else:
        return False




if __name__ == "__main__":
    main()