name = ["kelvin","tommy","andrea"]

def age():
	s = []
	for i in name:
		age1 = int(input(f"Enter your age {i}: "))
		s.append(age1)
	print(s)
	return s
	
age()
