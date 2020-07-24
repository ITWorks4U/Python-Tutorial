#!/usr/bin/python3

#	values to use
a = 10
b = 20

#	arithmetic operations
print("--- arithmetic operations ---")
print(a+b)
print(a-b)
print(a*b)
print(a/b)																					#	result may be a relational number
print(a//b)																					#	result is a decimal number only
print(a%b)
print(a**b)

#	comparisons
print("--- comparing operations ---")
print(a == b)																				#	for boolean output: use %s (string)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#	assignments
print("--- assigning operations ---")
result = a + b
print(result)

result += a																					#	equal to: result = result + a
print(result)

result -= b																					#	equal to: result = result - b
print(result)

result += 1																					#	Attention! In Python there is no result++
print(result)

#	bitwise operations
print("--- bitwise operations ---")
a = 0b1001001																				#	73
b = 0b101010																				#	42

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 4)
print(b << 4)

#	logical operations
a = True
b = False
print("--- locical operations ---")
print(a and b)																				#	similar to: intersection of a and b shall not be empty
print(a or b)																				#	similar to: union of a and b shall not be empty
print(not(a and b))																			#	¬(a and b) = ¬(a) ¬(and) ¬(b) = false or true = true

#	membership operations
a = 10
b = 20
tupleOfNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("--- membership operations ---")
print(a in tupleOfNumbers)																	#	claim, that a is a part ot the tuple: true
print(b in tupleOfNumbers)																	#	claim, that b is a part of the tuple: false
print(a not in tupleOfNumbers)
print(b not in tupleOfNumbers)

#	identity operations
print("--- identity operations ---")
print(a is b)																				#	claim, that a is identical to b: false
print(a is not b)
