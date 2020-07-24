#!/usr/bin/python3

#	working with functions

#aSimpleFunction()							#	won't work, because this function is not defined yet

'''
	A simple function without a parameter.
	By default, it returns nothing, which
	is equal to a void function in other
	programming languages
'''
def aSimpleFunction():						#	definition of a function
	print("I was called!")
# end function

for i in range(10):
	aSimpleFunction()						#	calling this function
# end for

#aSimpleFunction(1,2,3,4)					#	won't work, because our function takes 0 arguments only

'''
	Comes with a single argument only.
	A function in python may have more than
	one different return type.
'''
def aFunctionWithReturnValues(value):
	if value == 0:
		return bool(value)
	# end if

	if value == 1:
		return int(value)
	# end if

	if value == 2:
		return float(value)
	# end if

	if value == 3:
		return str(value)
	# end if

	return None
# end function

for i in range(5):
	retVal = aFunctionWithReturnValues(i)
	print(type(retVal))
# end for

'''
	Arbitrary arguments allows us to call a function
	with a different number of arguments.
	These are often shortened to *args in Python documentations.
'''
def arbitraryArguments(*args):
	print("Number of arguments: ", len(args))

	for i in args:
		print("argument:", i)
	# end for
# end function

arbitraryArguments("A", "B", "C")
arbitraryArguments(123)
arbitraryArguments()

'''
	Arbitrary keyword arguments are in use to
	handle with a dictionary. These are often
	shorened to *kwargs in Python documentations.
'''
def arbitraryKeywordArguments(**kwargs):
	for key in kwargs.keys():
		print(" Element: ", kwargs[key])
	# end for
# end function

arbitraryKeywordArguments(user = "ITWorks4U", location = "YouTube")

aSimpleList = [1, 2, 3, "A", "B", "C", False, 7, 5]
aNewDictionary = dict()

for i in range(0, len(aSimpleList)):
	aNewDictionary.update({str(i) : aSimpleList[i]})
# end for

arbitraryKeywordArguments(**aNewDictionary)

def aFunctionWithDefaultValues(defaultValue = "My own defined value!"):
	print(defaultValue)
# end function

aFunctionWithDefaultValues(123)
aFunctionWithDefaultValues("ABC")
aFunctionWithDefaultValues()