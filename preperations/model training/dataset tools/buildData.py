import os
import random
import sys

"""

This code builds the data files

"""

"""
excpects:
buildData.py all.txt folder_photos class_number folder_photos class_number folder_photos class_number ...
"""
def main():
	data = sys.argv[1:]
	all_file = data[0]
	data = data[1:]
	i = 1
	folder_val = {}
	while i < len(data):#extracting the directory and directory value
		folder_val[data[i-1]] = data[i]
		i+=2
	data = []
	for key in folder_val:#iterating through directories
		images = os.listdir(key)
		for img in images:#iterating teough images in directories
			data.append(key+img+' '+folder_val[key])
	random.shuffle(data)
	with open(all_file, 'w+') as f:#writing all the data into a file
		f.write('\n'.join(data))

if __name__ == '__main__':
    main()