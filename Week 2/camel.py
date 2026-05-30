text = input("camelCase: ")

for ch in text:
	if ch.isupper():
		text = text.replace(ch, "_"+ch.lower())

print(text)