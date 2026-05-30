greet = input("Greeting : ").strip().lower()

if greet[:5] == "hello":
	print("$0")
elif greet.startswith("h"):
	print("$20")
else:
	print("$100")