import os
import sys
"""

This code splits a file that contains all the data to
3 files

"""
def write(path, data):
	"""
	This function writes data to file
	input: file path, data to write
	output: non
	"""
	f = open(path, "w+")
	data = '\n'.join(data)
	f.write(data)
	f.close()

"""
excpects:
split.py all_data.txt train.txt percentage_in_float test.txt percentage_in_float val.txt
"""
def main():
	#extracting data given in call
	data = sys.argv[1:]
	data_file = data[0]
	train = data[1]
	train_am = float(data[2])
	test = data[3]
	test_am = float(data[4])
	val = data[5]
	#taking the data from the full file
	f = open(data_file, 'r')
	data = f.read().split('\n')
	f.close()
	l = len(data)
	#spliting the data to different arrays
	test_data = data[:int(l*test_am)]
	train_data = data[int(l*test_am):int(l*(test_am+train_am))]
	val_data = data[int(l*(test_am+train_am)):]
	#writing the splited data into different files
	write(val, val_data)
	write(test, test_data)
	write(train, train_data)

if __name__ == '__main__':
    main()