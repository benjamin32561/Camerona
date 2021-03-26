from uti import *

class beardClassifier():
	"""
	This class uses the beard classifier
	"""
	def __init__(self, model_path = "models/beard.h5"):
		"""
		This is the C'tor
		input: model path
		"""
		self.model = models.load_model(model_path)

	def checkBeard(self, people):
		"""
		This method uses the model to predict beards
		input: People object that contains the faces
		"""
		check = np.array(people.faces)
		#predicting
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):#iterating through predictions
			people.people[i].beard = predictions[i] < 0.5
		return people