from uti import *

class genderClassi():
	"""
	This class is the class that uses the gender classifier
	"""
	def __init__(self, model_path = "models/gender_best_model.h5"):
		self.model = models.load_model(model_path)

	def checkGenders(self, faces):
		#getting only the faces
		check = []
		for face in faces:
			check.append(face.face)
		check = np.array(check)
		predictions = self.model.predict(check)
		for i in range(0, len(predictions)):
			faces[i].gender = (predictions[i] < 0.5)
		return faces
