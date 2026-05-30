amount =50
while True:
	print("Amount Due:",amount)
	coin = int(input("Insert coin: "))

	if coin != 5 and coin != 10 and coin != 25:
		continue

	amount -= coin

	if amount <= 0:
		print("Change Owed:",-amount)
		break