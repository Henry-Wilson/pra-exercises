#This is a utilities function file.

#You will want to skip the first line either here or in
#main.py
def read_as_string_list( file_name ):
	"""
	This function is meant to return a list of all the lines in
	a file. You will have to modify it.
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
	for this to work.
	
	You do not have to modify this function.
	"""
	
	#Open file for WRITE
	the_file = open(file_name_destination, 'w', 1)
	#Dump JSON
	json.dump(compatible_object, the_file)
	return
