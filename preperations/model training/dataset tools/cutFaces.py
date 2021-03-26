import sys
import os
import cv2
from time import time
import numpy as np

"""

This code take a directory of images, cut the faces
 in each image and saves the faces

"""

class Coffe():
	def __init__(self, con_th = 0.8):
		tstamp = time()
		print('\n\n[COFFE] loading...')
		prototxtPath = "models/face-detection-weights.prototxt"
		weightsPath = "models/face-detection-model.caffemodel"
		self.net = cv2.dnn.readNet(prototxtPath, weightsPath)
		self.conf_th = con_th
		print('[COFFE] finished loading (%.4f sec)\n\n' % (time() - tstamp))

	def getFaces(self, img):
		(h, w) = img.shape[:2]

		blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))

		self.net.setInput(blob)
		detections = self.net.forward()[0][0]

		toRet = []
		for i in range(0, detections.shape[0]):
			confidence = detections[i][2]
			if confidence > self.conf_th:
				box = detections[i, 3:7] % np.array([1,1,1,1]) * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				(startX, startY) = (max(0, startX), max(0, startY))
				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

				start_point = (int(startX),int(startY))
				end_point = (int(endX),int(endY))
				if end_point[0] <= start_point[0]:
					end_point = (w, end_point[1])
				if end_point[1] <= start_point[1]:
					end_point = (end_point[0], h)
				face = img[start_point[1]:end_point[1], start_point[0]:end_point[0]]
				face = cv2.resize(face, (64,64))
				toRet.append(face)
		return toRet

"""
excpects:
cutFaces.py input_folder output_folder
"""
def main():
	data = sys.argv[1:]
	input_path = data[0]
	dst_path = data[1]
	i = len(os.listdir(dst_path)) + 1
	images = os.listdir(input_path)
	print(len(images))
	detector = Coffe()
	for image in images:#oterating through the images in a given directory
		full_input_path = os.path.join(input_path, image)
		img = cv2.imread(full_input_path)
		im = img
		faces = detector.getFaces(im)
		for face in faces:#iterating trough the faces found in image
			output_path = os.path.join(dst_path, str(i)+'.jpg')
			cv2.imwrite(output_path, face)
			i += 1

if __name__ == '__main__':
    main()