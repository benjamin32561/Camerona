import cv2


def drawBox(bbox, img):
	x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255),3,1)
	wid, hei = img.shape[:2]
	bbox = [[x/wid, y/hei],[(x+w)/wid, (y+h)/hei]]
	return bbox

def main():
	cap = cv2.VideoCapture(0)
	print("ds")
	_, img = cap.read()
	cap.release()
	while True:
		()
		bbox = cv2.selectROI("img", img, False)
		bbox = drawBox(bbox, img)
		print(bbox)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()