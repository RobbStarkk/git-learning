import math as m

def log2(x):
	return (m.log(x) / m.log(2)) 

print('Hi, I learning a git! This small program calculates the base 2 logarithm')
print("For example: log2(8.0) =")
print(log2(8.0))
print('Enter a number:')
a = input()
print(log2(a))
