text = input("Input: ")

for ch in text:
	if ch in "aeiou" or ch in "AEIOU":
		text = text.replace(ch, "")

print("Output:",text)