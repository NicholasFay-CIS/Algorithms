import sys
import string
from decimal import Decimal
#using Memoization


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
	while(W > 0):
		food_array[size[W]] += 1
		W -= v[size[W]]
	for i in range(0, len(food_array)):
		if(food_array[i] != 0):
			print("{} {}".format(s[i], food_array[i]))
	return 

def CMAXM(w, v, c, MCAL, size, n):
	"""
	int, list, list, list, list, int -> int
	returns the minimum amount of calories that we could eat
	"""
	if w == 0:
		return 0
	if MCAL[w] == sys.maxint:
		for i in range(0, n):
			if v[i] <= w:
				temp = CMAXM(w - v[i], v, c, MCAL, size, n)
				if(temp + c[i] < MCAL[w]):
					MCAL[w] = temp + c[i]
					size[w] = i
	return MCAL[w]

def main():
	#get the input file
	inputfile = sys.stdin
	sys.setrecursionlimit(1000000000)
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
	MCAL = [None] * (W + 1)
	#size = [None] * (W + 1)
	#set first index to be zero, (if w = 0, MCAL[w] = 0)
	MCAL[0] = 0
	#set the remaining indices to be negative infinity
	for i in range(1, W + 1):
		MCAL[i] = sys.maxint
	print("There are {} menu options".format(n))
	print("We want to spend {}".format(W))
	min_cal = CMAXM(W, v, c, MCAL, size, n)
	if(min_cal == sys.maxint):
		print("Not Possible to spend exactly: {}".format(W))
		return
	print("Possible to spend exactly: {}".format(W))
	print("Minimum Calories: {}".format(min_cal))
	find_items(size, food_array, W, v, s)

main()