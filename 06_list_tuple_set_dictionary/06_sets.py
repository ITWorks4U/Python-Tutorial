#!/usr/bin/python3

#	*****	sets		*****
aSimpleSet = {1, 2, 3, 7, 5, 3, None, "ABC", "DEF", "XYZ", "ABC"}					#	define a set
anEmptySet = set()																	#	an empty set

#	*****	accessing	*****
print(aSimpleSet)																	#	prints the whole set

for element in aSimpleSet:															#	using a loop
	print(element)
# end for

#	*****	modifiying	*****
aSimpleSet.add(False)																#	adding a new element to the set, if not already existing
aSimpleSet.pop()																	#	removing the last added element only

aSimpleSet.remove(7)																#	removing a given element, where this element MUST exist
aSimpleSet.discard(False)															#	try to remove a given element, if existing

print(aSimpleSet)

#	*****	have fun with sets	*****
A = {1, 2, 3, False, None}
B = {"A", "B", "C", 1, 2, 3}

print(A.union(B))																	#	A U B
print(A.intersection(B))															#	A ∩ B