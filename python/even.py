def evens(num):
	s = 0
	for i in num:
		if i % 2 == 0:
			s = i + s
	return s

evens([1, 2, 4])
x = evens([1,2,3,4,5,6])
print(x)
