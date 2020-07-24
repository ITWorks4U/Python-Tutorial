#!/usr/bin/python3

#	how to use loops in python3

a = 10

while a != 0:											#	start with a given condition check
	if a == 4:											#	also check, if a is equal to 4
		break											#	if true, then leave the last used loop
	# end if

	print(a)											#	prints the current value
	a -= 1												#	decrementing by one
# end while

#	---------------------------
print("---------------------------")
#	---------------------------

for i in range(a):										#	start from 0 to a-1 --> [0,3]
	print(i)											#	printing step i
# end for

#	---------------------------
print("---------------------------")
#	---------------------------

for i in (3,6,9,12,15,18):								#	using a defined tuple for our loop only
	if i % 2 == 0:										#	check, if element i is even
		continue										#	if true, then skip to the next element
	# end if

	print(i)											#	print element i
# end for

#	---------------------------
print("---------------------------")
#	---------------------------

for _ in range(a):										#	using _ if you don't need an element
	print("...")
# end for

#	---------------------------
print("---------------------------")
#	---------------------------

[print(i) for i in range(a)]							#	"press" everything into one line

#	---------------------------
print("---------------------------")
#	---------------------------

for pos,val in enumerate((3,6,9,12,15,18)):				#	using enumerate to handle with two variables
	print(pos, ":", val)								#	to reveal on which position is which element
# end for