text = input("Expression: ")

x,y,z = (text.split())

x= int(x)
z= int(z)

if y=="+":
	print(float(x+z))
elif y=="-":
	print(float(x-z))
elif y=="*":
	print(float(x*z))
elif y=="/":
	if y!=0:
		print(float(x/z))
	else:
		print("0 can not be the denominator!")
elif y=="%":
	print(float(x%z))
else:
	print("Error this is not an arithmetic operation: "+y)
