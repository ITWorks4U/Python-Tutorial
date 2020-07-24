#!/usr/bin/python3

#	how to handle with strings
aSimpleString = "A simple string!"
print(aSimpleString)

aSimpleString = 'Yeah, look at this!'
print(aSimpleString)

print("----------------------------------------")

#	---	accessing characters of a string	---
aSimpleString = "python3"

for c in aSimpleString:
	print(c)
# end for

#	---	get character at position n	---
print(" first element: ", aSimpleString[0])
print(" third element: ", aSimpleString[2])
print(" last element: ", aSimpleString[-1])

#	---	get characters between [n,k]	---
print(" aSimpleString[0:5]: ", aSimpleString[0:5])				#	[0:5]: "pytho", because we start from position 0 to position 5
print(" aSimpleString[0:-6]: ", aSimpleString[0:-6])			#	[0:-6]: "p"; you can also set a range from a positive number to a negative number
print(" aSimpleString[0:-7]: ", aSimpleString[0:-7])			#	[0:-7]: "", because there is no character in front of "p"

#	---	Strings are immutable!	---
# aSimpleString[4] = 'f'
# print(aSimpleString)
# del aSimpleString[3]
# print(aSimpleString)

print("----------------------------------------")

#	---	some functions for each string	---
print(aSimpleString.capitalize())								#	convert the string: starts with a capital character, every other character will be small
print(aSimpleString.isprintable())								#	returns true, if all characters are printable characters
print(aSimpleString.upper())									#	returns all alphanumerical characters in upper case

#	---	play with strings	---
joinString = "->".join(aSimpleString)							#	appending a "->"" between every character
print(joinString)

print(joinString.split('->'))									#	split a string -> create a list of character

print(aSimpleString + joinString)								#	concatenation of two or more strings

fiveWords = aSimpleString * 5
print(fiveWords)												#	multiple times of a string

print("Y" in aSimpleString)										#	check, if a character is somewhere in the string
print("f" in aSimpleString)
print(aSimpleString)