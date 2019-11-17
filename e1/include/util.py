#This is a utilities function file.

#You will want to skip the first line either here or in
#main.py
def read_as_string_list( file_name ):
	"""
	However one opens a file for READING in python,
	this function should do that and return the open
	file object. This may just be a wrapper of a
	single line of code, but the point of this
	exercise is not some arbitrary level of complexity.
	
	If this exercise insults your intelligence and you
	have been doing fileio in python for months or
	years, then I apologize. This is just where I felt
	like starting.
	"""
	
	#Read this page for info:
	#https://www.tutorialspoint.com/python/python_files_io.htm
	
	MODE = 'r' #READ mode
	BUFFERING = 1
	
	the_file = open(file_name, MODE, BUFFERING)
	the_list = []
	
	"""
	Your code goes here to read each line as a string
	and put all of those lines in the list.
	"""
	
	"""
	End your code here
	"""
	
	the_file.close()
	return the_list

"""
JSON prefers compatible_object to be a hierarchical python
dictionary. This should not be too hard. read
https://realpython.com/python-json/ for more info.
"""
def write_as_json( file_name_destination, compatible_object ):
	"""
	This function should take its input and write a file
	with a single JSON object contained, in standard
	JSON format.
	
	You will need to include JSON libraries in this file
	for this to work. Before you can do that, you will
	need to install said libraries with pip3.

	EDIT: No, you don't need to install the package. For
	some odd reason, python3 supports JSON internally.
	"""
	
	#Open file for WRITE
	the_file = open(file_name_destinaton, 'w', 1)
	#Dump JSON
	json.dump(compatible_object, the_file)
	return
