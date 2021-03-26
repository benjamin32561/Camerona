from uti import *

class maskClassifier():
	"""
	This class uses the mask classifier
	"""
	#mask - 1
	#no mask - 0
	def __init__(self, con_th = 0.8, model_path = "models/mask.h5"):
		"""
		this method is the C'tor
		input: min confidence to tell if a person is wearing a mask,
		the model path
		"""
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkMask(self, people):
		"""
		This method checks if given people wear a mask
		input: the people to check if
		output: new People object that contains only the people without a mask
		"""
		#taking only the faces
		check = np.array(people.faces)
		#predicting
		predictions = self.model.predict(check)
		toRet = People()
		for i in range(0, len(predictions)):
			if 1 - predictions[i] > self.conf_th:#checking if the prediction exeeds minimum requirments
				toRet.faces.append(people.faces[i])
				toRet.people.append(people.people[i])
		return toRet

class metaData():
	"""
	This class uses all the other model to extract data about the faces found
	"""
	def __init__(self, glass_path = "models/glass.h5", gender_path = "models/gender.h5", beard_path = "models/beard.h5"):
		"""
		This method is the C'tor
		input: models paths
		"""
		#index 0 - sunglass
		#index 1 - glass
		#index 2 - nothing
		self.glass_model = models.load_model(glass_path)
		#0 - female
		#1 - male
		self.gender_model = models.load_model(gender_path)
		#0 - no beard
		#1 - beard
		self.beard_model = models.load_model(beard_path)

	def getMetaData(self, people):
		"""
		This method uses the models to extract data
		input: people to extract data about
		output: the input object with updated data
		"""
		check = np.array(people.faces)
		#predicting 
		glass_prediction = self.glass_model.predict(check)
		gender_prediction = self.gender_model.predict(check)
		beard_prediction = self.beard_model.predict(check)
		for i in range(0, len(check)):#iterating through all the faces
			people.people[i].gender = gender_prediction[i] > 0.5#updating gender data
			people.people[i].beard = beard_prediction[i] > 0.5#updating beard data
			#updating glass data
			index = np.argmax(glass_prediction[i])
			people.people[i].sunglass = index == 0
			people.people[i].glass = index == 1
		return people