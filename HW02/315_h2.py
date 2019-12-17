import sys
import string
#Print_Paths inspired by geeksforgeeks and given DAG total path algorithm

def get_vertices(inputfile):
	"""
	FILE obj -> int
	returns the number of vertices in the list
	this also reads through the first line of the file
	"""
	return int(inputfile.readline())

def get_edges(inputfile):
	"""
	#FILE obj -> int
	returns the number of edges in the list
	this also reads through the second line of the file
	"""
	return int(inputfile.readline())

def copied_list(inputfile):
	"""
	FILE obj -> list
	This function copies the set of data from the input file
	"""
	copy = []
	for line in inputfile:
		line = line.split()
		copy.append(line)
	return copy

def Print_Paths(list__, nodes):
	"""
	list,int -> none
	This function find the shortest/longest path lengths as well
	as the number of short/long path lengths.

	print_Paths(list, 13)

	Shortest path: 6
	The number of short paths: 4
	Longest path: 8
	The number of long path: 16
	"""
	#create the arrays to store distances and frequency of paths (for distinct paths)
	short_paths = [None] * nodes
	long_paths = [None] * nodes
	distinct_short_paths = [None] * nodes
	distinct_long_paths = [None] * nodes

	#first index in arrays is set
	long_paths[0] = 0
	short_paths[0] = 0
	distinct_short_paths[0] = 1
	distinct_long_paths[0] = 1

	#second index in arrays is set
	long_paths[1] = 1
	short_paths[1] = 1
	distinct_short_paths[1] = 0
	distinct_long_paths[1] = 0

	#set up the value's for all the other index's 
	for i in range(2, nodes):
		long_paths[i] = 0
		short_paths[i] = 0
		distinct_short_paths[i] = 0
		distinct_long_paths[i] = 0

	#loop through the topologically sorted list
	#u is the vertex (left vert) and v is the right vertex with an edge between them
	for edge in list__:
		u = int(edge[0])
		v = int(edge[1])

		#for the shortest paths in the graph
		if(short_paths[v-1] == 0):
			short_paths[v-1] = short_paths[u-1] + 1

		if(short_paths[v-1] > short_paths[u-1] + 1):
			short_paths[v-1] = short_paths[u-1] + 1

		if(short_paths[v-1] == short_paths[u-1] + 1):
			distinct_short_paths[v-1] += distinct_short_paths[u-1] 

		#for the longest paths in the graph/distince paths
		if(long_paths[v-1] == 0):
			long_paths[v-1] = long_paths[u-1] + 1

		if(long_paths[v-1] < long_paths[u-1] + 1):
			long_paths[v-1] = long_paths[u-1] + 1

		#else we account for if (long_paths[v-1] == long_paths[u-1] + 1):
		else:
			distinct_long_paths[v-1] += distinct_long_paths[u-1]

	#get all the path numbers, which are the last element of each list
	short_ = short_paths[-1]
	long_ = long_paths[-1]
	shortd = distinct_short_paths[-1]
	longd = distinct_long_paths[-1]

	#Print to standard output.
	print("Shortest path: {} ".format(short_))
	print("The number of short paths: {}".format(shortd))
	print("Longest path: {}".format(long_))
	print("The number of long paths: {}".format(longd))
	return 


def main():
	"""
	None -> None
	This is the main function that runs the program
	"""
	#print("Starting program...")
	inputfile = sys.stdin
	#grabs the number of nodes/edges and reads the first two lines of the file
	vert = get_vertices(inputfile)
	edges  = get_edges(inputfile)
	#copies the remaining values of the input file
	list__ = copied_list(inputfile)
	#finds the paths
	Print_Paths(list__, vert)
	#print("Ending program...")
	return 

#call to main function
main()
