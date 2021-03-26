from uti import *

class ModelData():
	"""
	This class uses a tf-lite model to make predictions
	"""
	def __init__(self, model_path):
		"""
		This method is the C'tor
		input: model path
		"""
		self.model = tf.lite.Interpreter(model_path=model_path)#laoding model
		self.input_tensor_index = self.model.get_input_details()[0]['index']
		self.output_tensor_index = self.model.get_output_details()[0]['index']
		self.model.allocate_tensors()#allocating memory

	def modelPredict(self, face):
		"""
		This method uses the model to make predictions
		input: data to make predictions about
		output: the prediction
		"""
		self.model.set_tensor(self.input_tensor_index, face)
		self.model.invoke()
		prediction = self.model.get_tensor(self.output_tensor_index)
		return prediction

class metaData():
	"""
	This class uses the models to make prediction and extract data
	about the paople found in the picture
	"""
	def __init__(self,
		mask_path="models/mask.tflite", mask_con_th = 0.8,
		glass_path = "models/glass.tflite",
		gender_path = "models/gender.tflite",
		beard_path = "models/beard.tflite"):
		"""
		This method is the C'tor, loads all the models
		input: models paths and minimum threshold for the mask classifier
		"""
		#index 0 - sunglass
		#index 1 - glass
		#index 2 - nothing
		self.glass = ModelData(glass_path)
		#0 - female
		#1 - male
		self.gender = ModelData(gender_path)
		#0 - no beard
		#1 - beard
		self.beard = ModelData(beard_path)
		#0 - no mask
		#1 - mask
		self.mask = ModelData(mask_path)
		self.mask_th = mask_con_th

	def getMetaData(self, people):
		"""
		This method uses the models to extract data
		input: People object, contains faces and Person object wich contains data
		output: updated People object contains updated data
		"""
		to_ret = People()
		j = 0
		for i in range(0, len(people.faces)):#iterating through all the faces
			face = people.faces[i]
			#checking mask
			prediction = self.mask.modelPredict(face)[0][0]#making prediction for face
			if 1 - prediction > self.mask_th:#checking if not wearing a mask
				to_ret.faces.append(people.faces[i])
				to_ret.people.append(people.people[i])
				#checking beard
				prediction = self.beard.modelPredict(face)[0][0]#checking for a beard
				to_ret.people[j].beard = prediction > 0.5
				#checking gender
				prediction = self.gender.modelPredict(face)[0][0]#checking for gender
				to_ret.people[j].gender = prediction > 0.5
				#checking glass
				prediction = self.glass.modelPredict(face)[0]#checking glass type
				index = np.argmax(prediction)
				to_ret.people[j].sunglass = index == 0
				to_ret.people[j].glass = index == 1

				j += 1
		return to_ret