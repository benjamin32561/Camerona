import tensorflow as tf

#this code is used to convert .h5 file to .tflite

saved_at = "mask.h5"
save_at = "mask.tflite"

#loading the model
model = tf.keras.models.load_model(saved_at)
#converting keras to tflite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]#setting optimizations
tflite_model = converter.convert()
open(save_at, "wb").write(tflite_model)#saving the tflite model