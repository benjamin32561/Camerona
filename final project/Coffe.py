from uti import *

class Coffe():
	"""
	This class uses the opencv model to detect faces in a photo
	"""
	def __init__(self, con_th = 0.8):
		"""
		This method is the C'tor
		input: minimum confidence to determine if something is a face
		"""
		prototxtPath = "models/face-detection-weights.prototxt"
		weightsPath = "models/face-detection-model.caffemodel"
		self.net = cv2.dnn.readNet(prototxtPath, weightsPath)
		self.conf_th = con_th

	def detectFaces(self, img):
		"""
		This method uses the model to detect the faces in a picture
		"""
		(h, w) = img.shape[:2]

		blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))

		self.net.setInput(blob)
		detections = self.net.forward()[0][0]

		toRet = People()
		for i in range(0, detections.shape[0]):#iterating through faces found in the picture
			confidence = detections[i][2]
			if confidence > self.conf_th:#checking if the face exeeds the minimum confidence
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
				face = cv2.resize(face, (64,64))/255
				face = np.array([face], dtype=np.float32)#changing the data to float32
				#adding the person found to the people object
				toRet.people.append(Person(start_point, end_point))
				toRet.faces.append(face)
		return toRet