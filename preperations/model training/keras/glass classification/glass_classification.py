from tensorflow.keras import models
import numpy as np

class glassClassifier():
	"""
	This class uses the glass classifier
	"""
	#index 0 - sunglass
	#index 1 - glass
	#index 2 - nothing
	def __init__(self, model_path = "models/glass-model.h5"):
		"""
		This is the C'tor
		input: model path
		"""
		self.model = models.load_model(model_path)

	def checkGlassType(self, people):
		"""
		This method uses the model to predict glass type
		input: People object that contains the faces
		"""
		check = np.array(people.faces)
		#predicting
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):#iterating through predictions
			index = np.argmax(predictions[i])
			people.people[i].sunglass = index == 0
			people.people[i].glass = index == 1
		return people