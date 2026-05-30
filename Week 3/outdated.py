# In a file called outdated.py, implement a program that prompts the user for a date,
# anno Domini, in month-day-year order, formatted like 9/8/1636 or
# September 8, 1636, wherein the month in the latter might be any of the values in the list below:
# Output: YYYY-MM-DD
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
	try:
		date = input("Date: ").strip()

		if date.find("/") != -1:
			a,b,c = date.split("/")
			a=int(a)
			b=int(b)
			if not (1 <= a <= 12 and 1 <= b <= 31):
				continue
			print(f"{c}-{a:02}-{b:02}")
			break

		elif date.find(",") != -1:
			a,b,c = date.split(" ")
			if a in month:
				MM = month.index(a)+1
				b= int(b.replace(",",""))
				if not (1 <= b <= 31):
					continue
				print(f"{c}-{MM:02}-{b:02}")
				break
			else:
				continue

		else:
			continue

	except (ValueError,NameError):
		pass

