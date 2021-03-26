from Coffe import *
from classifiers import *
import datetime
import time

PLAY_FROM = 0#vid.mp4

ATT_LIMIT = 10

FACES_CONF_TH = 0.9
MASK_CONF_TH = 0.9

BOUNDING_BOX_COLOR = (0,0,255)
TEXT_COLOR = (255,255,255)
TEXT_COLOR_OVER_LIMIT = (0,0,255)
LINE_THICKNESS = 2
FONT = cv2.FONT_HERSHEY_SIMPLEX

#models paths
MASK_PATH = 'models/mask.tflite'
GENDER_PATH = 'models/gender.tflite'
GLASS_PATH = 'models/glass.tflite'
BEARD_PATH = 'models/beard.tflite'

def drawNoMasks(people, img):
	"""
	This function draw the boxes and data about each face in a photo
	input: the data about the people found, the image
	output: non
	"""
	cnt = 1
	txt_clr = TEXT_COLOR
	for face in people.people:
		cv2.rectangle(img, face.start_pnt, face.end_pnt, BOUNDING_BOX_COLOR, LINE_THICKNESS)
		text = 'F'
		if face.gender or face.beard:
			text = 'M'
		if face.glass:
			text += ' G'
		elif face.sunglass:
			text += ' SG'
		if face.beard:
			text += ' B'
		if cnt > ATT_LIMIT:
			txt_clr = TEXT_COLOR_OVER_LIMIT
		text += ' ' + str(cnt)
		cnt+=1
		cv2.putText(img, text, (face.start_pnt[0], face.end_pnt[1]), FONT, 1, txt_clr, LINE_THICKNESS)

def main():
	#loading models
	face_detector = Coffe(FACES_CONF_TH)
	metadata_models = metaData(MASK_PATH, MASK_CONF_TH, GLASS_PATH, GENDER_PATH, BEARD_PATH)
	#loading video data
	cap = cv2.VideoCapture(PLAY_FROM)
	time_started = time.time()
	frames = 0
	while True:
		#iterating through the video, frame by frame
		work, frame = cap.read()
		if not work:
			#checking if the video ended
			break
		#detecting faces
		people = face_detector.detectFaces(frame)
		if len(people.faces) > 0:
			#extracting metadata from faces
			people = metadata_models.getMetaData(people)
			drawNoMasks(people, frame)
		cv2.imshow('show', frame)
		frames += 1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	overall_time = time.time() - time_started
	print("avg frames pre second: {0}".format(frames/overall_time))
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()