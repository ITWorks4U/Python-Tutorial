#!/usr/bin/python3

#	How to understand the datatype none in Python

undefinedObject = None
print("You will see this:", undefinedObject)
print("-----------------------")

"""
	In Python none is defined as a null value,
	similar to C/C++ (pointers), Java, C# as null.
	It also shows no value at all.

	None isn't the same like false, 0 or an empty string. It's
	an unique data type to define an undefined state of an object.
"""

stringObject = "Test string"

#	What will happen? Do we receive an error?
print("Are these both objects equal? {0}".format(undefinedObject.__eq__(stringObject)))
print("Are these both objects equal? {0}".format(stringObject == undefinedObject))
print("Are these both objects equal? {0}".format(stringObject is undefinedObject))
print("-----------------------")

#	define none for functions
def nonsenseFunction():
	pass
# end function

print(nonsenseFunction())
print("-----------------------")

#	rember: in python a function can return multiple types of objects
def receiveAnyValue(value: int):
	if value == 1:
		return value
	elif value == 2:
		return str(2) 

	return None
# end function

print(receiveAnyValue(1))
print(receiveAnyValue(2))
print(receiveAnyValue(3))