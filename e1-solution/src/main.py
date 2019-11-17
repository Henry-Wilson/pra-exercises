#This is the main loop of our parsing program.
#You will need to include our util.py file.

#Recommend using sys to add its directory to
#your path, then including plainly.
import sys
#Fill the following string with the RELATIVE path
#to the directory containing util.py
sys.path.insert(0,'../include')
import util

if __name__ == '__main__':
	"""
	This should read a file in, then write its
	data out to a series of JSON files, e.g,
	telem1.json, telem2.json ....
	"""
	data_in_file = '../data/d1.txt' #Fill with relative path
	
	data_out_name = '../data/telem'
	data_out_num = 1
	data_out_extension = '.json'
	
	#Finish the following line with a function
	#from util.py
	lines_from_file = util.read_as_string_list( data_in_file )
	
	#You will want to skip the first line either
	#here or in the file reader.
	for line in lines_from_file:
		"""
		Grab data from the line, put it into a
		dictionary.
		
		Concatenate data_out parts into a file
		path, then write the dictionary to the
		file with util method.
		
		increment data_out_num.
		"""
		rawdat = line.split(',')
		json_dict = {
			"telem" : {
				"altitude" : float(rawdat[0]),
				"longitude" : float(rawdat[1]),
				"latitude" : float(rawdat[2]),
				"heading" : float(rawdat[3])
			}
		}
		data_out_file = data_out_name + str(data_out_num) + data_out_extension
		util.write_as_json( data_out_file, json_dict )
		data_out_num += 1
