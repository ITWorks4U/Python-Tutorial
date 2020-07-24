#!/usr/bin/python3

#	interaction example with the machine

'''
readContent = input(" give an argument: ")			#	enter anything, which is going to convert to a string by default
print(readContent)
print(type(readContent))
'''

'''
readInputAsNumber = input(" give me a number: ")	#	read anything
readInputAsNumber = int(readInputAsNumber)			#	try to convert this input to an intege, IF possible
print(readInputAsNumber)
print(type(readInputAsNumber))
'''

a,b = [int(i) for i in input(" give me two numbers: ").split()]
print("product of a*b is ", (a*b))