while True:
	try:
		text = input("Fraction: ")
		x,z = text.split("/")
		x=int(x)
		z=int(z)
		if x > z or x<0 or z<0:
			continue
		result = round( (x/z) * 100)
		if result <= 1:
			print("E")
		elif result >= 99:
			print("F")
		elif 1<result<99:
			print(f"{result}%")
		else:
			continue
		break
	except (ValueError,ZeroDivisionError):
		pass


