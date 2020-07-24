#!/usr/bin/python3

#	*****	tuples		*****
aSimpleTuple = (7,5,3, True, False, "Hello World!")							#	define a tuple with fixed elements
anEmptyTuple = tuple()														#	define an empty tuple

#	*****	accessing	*****
print(aSimpleTuple)															#	print the whole tuple

for element in aSimpleTuple:												#	using a loop
	print(element)
# end for

print(aSimpleTuple.count(True))												#	count how often an element exists in our tuple
print(aSimpleTuple.index(True))												#	get the position of an element

#	*****	modifiying	*****
'''
	A tuple is a fixed structure. It won't allows us
	to modify the elements.
'''

#	*****	have fun with tuples	*****
t = (1,2,3)																	#	define a new tuple
(a, b, c) = t																#	refering a tuple of variables to tuple t

if (a,b,c) == (1,2,3):														#	let compare (a,b,c) with (1,2,3)
	print("Hooray")
# end if