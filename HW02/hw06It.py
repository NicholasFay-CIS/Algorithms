import sys
import string
from decimal import Decimal
#using iteration

def get_options(inputfile):
	"""
	FILE obj->int
	This gets the amount of options from the input file
	"""
	return int(inputfile.readline())

def get_amount(inputfile):
	"""
	FILE obj->int
	This gets the budget from the input file
	"""
	return int(inputfile.readline())

def createlists(inputfile, v, c, s):
	"""
	FILE obj->list
	This function copies the set of data from the input file into
	the value and calorie arrays
	"""
	for line in inputfile:
		line = line.split()
		v.append(int(line[0]))
		c.append(int(line[1]))
		s.append(line[2])
	return 

def find_items(size, food_array, W, v, s):
	"""
	list,list,int,list,list -> None
	This function will determine exactly how much of
	what food items we need to reach our exact cost
	"""
	#while our budget is not zero
	while(W > 0):
		#update the frequency table and subtract the cost from W
		food_array[size[W]] += 1
		W -= v[size[W]]
	for i in range(0, len(food_array)):
		#loop through the frequency array and if there is not a zero, print it
		#and print the food item corresponding to it
		if(food_array[i] != 0):
			print("{} {}".format(s[i], food_array[i]))
	return 

def CMIN(W, v, c, n, size):
	"""
	int,list,list,int,list -> int
	This function will return the min number of calories we can eat with our cost W
	"""
	#MCAL is length of W
	MCAL = [None] * (W + 1)
	#size is defined in the main function
	#set first index to be zero, (if w = 0, MCAL[w] = 0)
	MCAL[0] = 0
	#set the remaining indices to be negative infinity
	for i in range(1, W + 1):
		MCAL[i] = sys.maxint
	#loop through our possible budget
	for i in range(1, W + 1):
		#loop through all the options
		for j in range(0, n):
			#if the cost of some item at index j
			#is less than our current budget
			if(v[j] <= i):
				#if we find a new min value then update 
				if(MCAL[i] > (MCAL[ i - v[j] ] + c[j])):
					MCAL[i] = (MCAL[ i - v[j] ] + c[j])
					size[i] = j
	#Not possible with the given amount
	#if our budget is too small it is not possible.
	if(MCAL[W] == sys.maxint):
		print("Not possible to spend exactly: {}".format(W))
		return -1
	print("Possible to spend exactly: {}".format(W))
	return MCAL[W]

def main():
	#get the input file
	inputfile = sys.stdin
	#sets up arrays for the cost, calories
	x = sys.maxint
	v = []
	c = []
	s = []
	#number of menu items and the amount we want to spend
	n = get_options(inputfile)
	W = get_amount(inputfile)
	size = [x] * (W + 1)
	food_array = [0] * n
	#create lists for v and c
	createlists(inputfile, v, c, s)
	#get the min calories
	#print("There are {} menu options".format(n))
	#print("We want to spend {}".format(W))
	min_cal = CMIN(W, v, c, n, size)
	if(min_cal >= 0):
		print("Minimum Calories: {}".format(min_cal))
	if(min_cal == -1):
		return
	find_items(size, food_array, W, v, s)

main()
