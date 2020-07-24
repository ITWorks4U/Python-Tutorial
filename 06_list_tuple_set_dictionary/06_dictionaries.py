#!/usr/bin/python3

#	*****	dictionaries	*****
aSimpleDictionary = {												#	define a dictionary
	'red' : 0xFF0000,
	'yellow' : 0xFFFF00,
	'green' : 0xFF00,
	'blue' : 0xFF
}

anEmptyDictionary = dict()											#	define an empty dictionary

#	*****	accessing		*****
print(aSimpleDictionary)											#	print the whole dictionary

for key in aSimpleDictionary.keys():								#	using a loop
	print(hex(aSimpleDictionary[key]))

#	*****	modifiying		*****
aSimpleDictionary.update({'white' : 0xFFFFFF, 'black' : 0})			#	add n elements to the dictionary
aSimpleDictionary.pop('yellow')										#	removing an element somewhere in the dictionary by given key
aSimpleDictionary.popitem()											#	removing the last element from the dictionary

print(aSimpleDictionary)

#	*****	have fun with dictionaries	*****
print(aSimpleDictionary.keys())										#	get the keys
print(aSimpleDictionary.values())									#	get the values
print(aSimpleDictionary.items())									#	print each element from the dictionary as a list of tuples

#	*****	converting a list to a dictionary	*****
aSimpleList = [1, 2, 3, "A", "B", "C", False, 7, 5]					#	first way to convert a list to a dictionary
iterator = iter(aSimpleList)
aNewDictionary = dict(zip(iterator, iterator))
print(aNewDictionary)

aNewDictionary.clear()												#	removing all elements

for i in range(0, len(aSimpleList)):								#	second way to convert a list to a dictionary
	aNewDictionary.update({i : aSimpleList[i]})
# end for

print(aNewDictionary)