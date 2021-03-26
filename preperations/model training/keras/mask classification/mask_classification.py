from uti import *

class maskClassifier():
	"""
	This class uses the mask classifier
	"""
	#mask - 1
	#no mask - 0
	def __init__(self, con_th = 0.8, model_path = "models/mask.h5"):
		"""
		This is the C'tor
		input: minimum confidence, model path
		"""
		self.model = models.load_model(model_path)
		self.conf_th = con_th

	def checkMask(self, people):
		"""
		This method uses the model to predict weather the person wears a mask or not
		input: People object contains faces to check
		"""
		check = np.array(people.faces)
		#predicting
		predictions = self.model.predict(check)
		toRet = People()
		for i in range(0, len(predictions)):#iterating through predictions
			if 1 - predictions[i] > self.conf_th:
				toRet.faces.append(people.faces[i])
				toRet.people.append(people.people[i])
		return toRet