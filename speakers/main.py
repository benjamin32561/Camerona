from Coffe import *
from classifiers import *
from use_speakers import *
from datetime import datetime
import time
import os

ATT_LIMIT = 5
OVER_LIMIT_FOLDER = "over_limit/"
NO_MASK_FOLDER = "no_mask/"

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

#models paths
MASK_PATH = 'models/mask.tflite'
GENDER_PATH = 'models/gender.tflite'
GLASS_PATH = 'models/glass.tflite'
BEARD_PATH = 'models/beard.tflite'

def addressPeople(people, now):
	"""
	This function tells people to wear a mask
	input: the data about the people found, the time when the picture was taken
	output: non
	"""
	cnt = 1
	i = 0
	while i < len(people.people):
		person = people.people[i]
		face = np.array(people.faces[i][0]*255,dtype=np.uint8)#changing the dtype so it will be visible
		play(person)#playing sound
		file_name = NO_MASK_FOLDER + now + '_' + str(cnt) +'.jpg'
		cv2.imwrite(file_name, face)
		i+=1

def main():
	#loading models
	face_detector = Coffe(FACES_CONF_TH)
	metadata_models = metaData(MASK_PATH, MASK_CONF_TH, GLASS_PATH, GENDER_PATH, BEARD_PATH)
	#loading video data
	cap = cv2.VideoCapture(0)
	while True:
		#iterating through the video, frame by frame
		work, frame = cap.read()
		#detecting faces
		people = face_detector.detectFaces(frame)
		now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		if len(people.people) > ATT_LIMIT:
			file_name = OVER_LIMIT_FOLDER + now + '.jpg'
			cv2.imwrite(file_name, frame)
		if len(people.faces) > 0:
			#extracting metadata from faces
			people = metadata_models.getMetaData(people)
			addressPeople(people, now)

if __name__ == '__main__':
	main()