#!/usr/bin/python3

#################################
#	read content from a file	#
#################################

#	first option to read a file:
fileToUse = open("08_file_IO/lorem_ipsum.txt", "r")					#	by using open() we can read a file
for line in fileToUse:												#	and prints the whole content line by line
	print(line)
#end for
fileToUse.close()													#	closes the file stream

print("\n---------------------\n")
#	second option to read a file:
fileToUse = open("08_file_IO/lorem_ipsum.txt", "r")
print(fileToUse.read())												#	using the method read() instead
fileToUse.close()

print("\n---------------------\n")
#	third option to read a file:

with open("08_file_IO/lorem_ipsum.txt", "r") as fileToUse:			#	using with command instead
	print(fileToUse.read())
# end with
fileToUse.close()

#############################
#	write content to a file	#
#############################

#	first option to write to a file:
outputFile = open("08_file_IO/result.txt", "w")						#	write to this file
outputFile.write("This is our first line!\n")
outputFile.writelines([str(i) for i in range(10)])
outputFile.close()

#	second option to write to a file:
with open("08_file_IO/result.txt", "a") as outputFile:
	outputFile.write("\n")
	outputFile.writelines([str(i) for i in range(10)])
# end with
outputFile.close()