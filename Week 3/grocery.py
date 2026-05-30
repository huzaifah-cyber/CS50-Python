groceries = {}

while True:

	try:
		item = input().lower()

		if item in groceries:
			groceries[item] += 1
		else:
			groceries[item] = 1
	except EOFError:
		sorted(groceries)
		for item in sorted(groceries):
			print(groceries[item],item.upper())

		break