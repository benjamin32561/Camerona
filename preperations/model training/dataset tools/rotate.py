import cv2
import imutils
import os
import sys
import numpy as np

"""

this code rotetes all the photos in a given directory

"""

"""
excpect:
rotate.py input_folder output_folder
"""
def main():
	#extracting input and output directories
	data = sys.argv[1:]
	input_path = data[0]
	dst_path = data[1]
	images = os.listdir(input_path)
	i = len(os.listdir(dst_path)) + 1
	j = 1
	for image in images:#iterating through images
		if j%100 == 0:
			print("{0}/{1}".format(j, len(images)))
		j += 1
		full_input = os.path.join(input_path, image)
		im = cv2.imread(full_input)#loading base image
		full_output = os.path.join(dst_path, str(i)+'.jpg')
		os.rename(full_input, full_output)
		i += 1
		for angle in np.arange(10, 30, 5):#rotating the image
			rotated = imutils.rotate(im, angle)
			full_output = os.path.join(dst_path, str(i)+'.jpg')
			cv2.imwrite(full_output, rotated)#saving rotated image
			i += 1
		for angle in np.arange(330, 360, 5):#rotating the image
			rotated = imutils.rotate(im, angle)
			full_output = os.path.join(dst_path, str(i)+'.jpg')
			cv2.imwrite(full_output, rotated)#saving rotated image
			i += 1

if __name__ == '__main__':
    main()