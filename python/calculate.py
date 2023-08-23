def calculate(sign, nam1, nam2 ):
	
	if sign == "add" or "Add" or "ADD":
		print(nam1 + nam2)
	elif sign == "multiply" or "Multiply" or "MULTIPLY":
		print(nam1 * nam2)
	elif sign == "subtract" or "Subtract" or "SUBTRACT":
		print(nam1 - nam2)
	elif sign == "divide" or "Divide" or "DIVIDE":
		print(nam1 / nam2)
	else:
		print("invalid input")
	
sign = input("Enter name of a sign: ")
nam1 = int(input("Enter your first number: "))
nam2 = int(input("Enter the second number: "))

calculate(sign,nam1,nam2)
