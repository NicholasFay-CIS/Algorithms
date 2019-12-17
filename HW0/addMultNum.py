import sys
import string

def addMultNum():
	"""
	None -> None
	This function reads the information in a file 
	prints the addition of the two numbers and their multiplication
	returns none

	addmultnum()
	>>>
	"""
	#sets the standard input to a variable
	inputfile = sys.stdin
	#reads the first line of the input so it does not get included in the calculations
	inputfile.readline()
	for line in inputfile:
		#seperate the lines in lists
		line = line.split()
		#add the two numbers
		add = int(line[0]) + int(line[1])
		#multiply the two numbers
		mul = int(line[0]) * int(line[1])
		#print them out
		print("{} {}".format(add, mul))
	return


def main():
	#call to function
	addMultNum()
	return

	
#call to main
main()
