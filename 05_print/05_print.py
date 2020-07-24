#!/usr/bin/python3

#	how to handle with the print function

print()																	#	prints an empty line by default
print("123ABC")															#	using double quotas
print('123ABC')															#	or single qoutas to print a text

print("--------------------------------")

stringVal = "This is a string."
numberVal = 100
booleanVal = False

print(stringVal,numberVal,booleanVal)									#	print every variable including commata
print(stringVal + str(numberVal) + str(booleanVal))						#	do a concatenation of two or more >>words<<

print("--------------------------------")

print("%s" % stringVal)													#	formatting argument as a word
#print("%d" % stringVal)												#	won't work
print("%s %d %s" % (stringVal, numberVal, booleanVal))					#	print multiple arguments by given formatting characters in a specified sequence

print("--------------------------------")

print("{}, {}, {}".format(stringVal, numberVal, booleanVal))			#	let the formatting be done by the system
print("{2}, {0}, {1}".format(stringVal, numberVal, booleanVal))			#	determine on which position is which argument