#!/usr/bin/python3

#	How to understand and use recursion in Python

"""
	A recursion is a function, which runs forever (in theory), unless
	a condition check returns true, thus the recursion ends.

	This construct is much faster than a loop, like for, do, while, until, ...,
	but the memory usage is much more bigger, however, mostly a recursion
	is more often used than a loop, because it contains less code including
	a bit hard to understand.
"""

def aRecursiveFunction(number):
	if number == 0:															#	in a recursion WE MUST HAVE a condition check to leave the funtion
		return number														#	otherwise our program will run forever (in theory)

	print("Current number:", number)
	return aRecursiveFunction(number - 1)									#	while our condition is not satisfied, then we do other stuff
# end function

print(aRecursiveFunction(10))
print("-----------------------")

def Fibonacci(number):
	if number == 0 or number == 1:
		return number

	return (Fibonacci(number - 1) + Fibonacci(number - 2))
# end function

print(Fibonacci(10))
print(Fibonacci(20))
print(Fibonacci(30))
print(Fibonacci(40))
print("-----------------------")