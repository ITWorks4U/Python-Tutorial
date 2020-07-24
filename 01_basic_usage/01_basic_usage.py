#!/usr/bin/python3																										#	shebang command

print("Hello World!")																									#	simple print command
print("1, 2, 3")

number = 123																											#	declaring as an integer
print(number)

number = 123.456789																										#	now it's a float type
print(number)

number = str(number)																									#	convert it to a word
print(number)

#--------------------------

#	a simple single line commentary

'''
	a multiline commentary;
	it allows you to show more details
'''

"""
	also a multiline commentary;
	important: the types of the starting quotas
	and ending quotas must be equal and should not
	be inside of this commentary
"""

#"""
#	a bad example of commentary; let's say,
#	you're using """ inside of your commentary,
#	then pyton declares this as an error on runtime
#"""

#--------------------------

'''
	Python comes with a dynamic interpretation of types,
	however, it also contains data types for a
	special purpose
	
	with type(a_given_type) you can get the type
'''

print(type(10))																											#	integer
print(type(12345.6789))																									#	float type
print(type("ABC"))																										#	string type
print(type(True))																										#	boolean type
print(type(None))																										#	like NULL in C/C++
print(type([1,2,3]))																									#	list type
print(type({1,2,3}))																									#	set type
print(type({1:'A', 2:'B', 3:'C'}))																						#	dictionary type
print(type((1,2,3)))																									#	tuple type
