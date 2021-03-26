Couldnt import the git lab repo so I copied all the files into here... link to the git lab repo https://gitlab.com/benjamin32561/camerona.git

# Camerona

Camerona - A combination of the words 'camera' and 'corona', this tool may help with the enforcement of wearing masks during covid-19

## Quick explanation

The idea of the project is to find people who doesnt wear mask in a photo, extract data about them and then address them by asking to wear a mask using the data the progrm found about each person.

## Models
Me and my partner built and trained our model by ourselves using tensorflow and data we found online.
we built 4 models:
First model is being used to determine if the person is wearing a mask (Binary classification).
Second model is predicting the gender of a person (Binary classification).
Third model is predicting if the person has a beard (Binary classification).
Fourth model is predicting if the person has sunglass, regular glasses or non at all (multi-class classification).

We also tried to build and train our own SSD model for face detection but failed.

### Models architectures

![Mask classifier architecture](preperations/model training/keras/mask classification/maskModel.png?raw=true "Mask classifier")
![Gender classifier architecture](preperations/model\ training/keras/gender\ classification/genderModel.png?raw=true "Gender classifier")
![Beard classifier architecture](preperations/model\ training/keras/beard\ classification/beardModel.png?raw=true "Mask classifier")
![Glass classifier architecture](preperations/model\ training/keras/glass\ classification/glassModel.png?raw=true "Mask classifier")

## Main files

keras/main.py is using tensorflow models to make prediction, the predictions are displayed on a video window.
tf-lite/main.py is using tensorflow lite models to make prediction, the predictions are displayed on a video window.
speakers/main.py is using the tensorflow lite models to predict and use the speakers to address some one.
