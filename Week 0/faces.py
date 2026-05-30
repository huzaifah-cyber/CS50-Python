def convert(input_by_user):
	return input_by_user.replace(":)","\U0001F642").replace(":(","\U0001F641")

def main():
	print(convert(input()))

main()