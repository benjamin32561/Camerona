from tensorflow.keras import models
import numpy as np
import cv2
from time import time, sleep
import numpy as np

class People():
	"""
	This class represents the People found, contains faces and other data
	"""
	def __init__(self):
		self.faces = []
		self.people = []

class Person():
	"""
	This class represents a single persin found, contains data about it
	"""
	def __init__(self, startPoint, endPoint):
		self.start_pnt = startPoint #start point of his face in the picture
		self.end_pnt = endPoint #end point of his face in the picture
		self.gender = False
		self.glass = False
		self.sunglass = False
		self.beard = False