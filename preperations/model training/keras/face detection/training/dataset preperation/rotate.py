import cv2
from Coffe import *
import imutils

def main():
	face_detector = Coffe(0.65)
	path = "data\\"
	dst = "data1\\"
	i = len(os.listdir(dst)) + 1
	j = 0
	images = os.listdir(path)
	for image in images:
		if j%100 == 0:
			print("{0}/{1}".format(j, len(images)))
		j += 1
		input_path = os.path.join(path, image)
		im = cv2.imread(input_path)
		im2 = im
		faces_found = face_detector.countFaces(im2)
		output_path = os.path.join(dst, str(i)+'.jpg')
		os.rename(input_path, output_path)
		i += 1
		for angle in np.arange(3, 30, 3):
			rotated = imutils.rotate(im, angle)
			rotated2 = rotated
			if face_detector.countFaces(rotated2) == faces_found:
				output_path = os.path.join(dst, str(i)+'.jpg')
				cv2.imwrite(output_path, rotated)
				i += 1
		for angle in np.arange(330, 360, 3):
			rotated = imutils.rotate(im, angle)
			rotated2 = rotated
			if face_detector.countFaces(rotated2) == faces_found:
				output_path = os.path.join(dst, str(i)+'.jpg')
				cv2.imwrite(output_path, rotated)
				i += 1

if __name__ == '__main__':
    main()