#!/usr/bin/python3

#	let's have two values
a = 10
b = 20

'''
	VERY IMPORTANT:
		- condition checks (also for loops, functions and classes)
		  must have an indentation (white space OR tabs only)

		- do NOT merge your python code with both intendentions,
		  it's a syntax error

		- be careful, which code is a part of a condition check (also
		  for a loop, a function or a class); means: every code, which has
		  the same indentation like the last code above, is automatically
		  a part of this condition, loop, etc.

		- every special block of code (condition, loop, etc.) must have
		  at least a code; it's a syntax error, if this field is empty;
		  even a commentary as a dummy holder is also not valid;
		  if an implementation is in further use, then use the keyword: pass

		- if you're not sure about the indentations in your code, then you
		  can activate the white spaces, depending on the editor you're using

		- hint: it's not required, but for a better design and reading, mark
		  your indentation at the end with an commentary, like: #end if, #end for or else
'''
if a == b:
	print("a is equal to b")
# end if

if a != b:
	print("a is not equal to b")
# end if

if a != b:
	pass
# end if

if a == b:
	print("both values are equal")
elif a != b:
	print("both values are not equal")
else:
	print("...")
# end if
