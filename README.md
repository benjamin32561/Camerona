Couldnt import the git lab repo so I copied all the files into here... link to the git lab repo https://gitlab.com/benjamin32561/camerona.git

# Camerona

Camerona - A combination of the words 'camera' and 'corona', this tool may help with the enforcement of wearing masks during covid-19

## Quick explanation

The idea of the project is to find people who doesnt wear mask in a photo, extract data about them and then address them by asking them to wear a mask based on the data found about each person.

## Models
Me and my partner built and trained our model by ourselves using tensorflow and data we found online.
we built 4 models:
First model is being used to determine if the person is wearing a mask (Binary classification).
Second model is predicting the gender of a person (Binary classification).
Third model is predicting if the person has a beard (Binary classification).
Fourth model is predicting if the person has sunglass, regular glasses or non at all (multi-class classification).

We also tried to build and train our own SSD model for face detection but failed.

### Models architectures

![Mask classifier architecture](./preperations/model training/keras/mask classification/maskModel.png)

![Gender classifier architecture](https://github.com/benjamin32561/Camerona/tree/master/preperations/model%20training/keras/gender%20classification/genderModel.png)

![Beard classifier architecture](https://github.com/benjamin32561/Camerona/tree/master/preperations/model%20training/keras/beard%20classification/beardModel.png)

![Glass classifier architecture](https://github.com/benjamin32561/Camerona/tree/master/preperations/model%20training/keras/glass%20classification/glassModel.png)

As you can see the model are fairly simple, They have to be simple in order to avoid overfitting to the training data.

### Training

The training took some time, I used [Weights & Biases](https://wandb.ai/site) to track the training of each model.

You can see the training graphs in each of the models trainging folder:

[Mask graph](https://github.com/benjamin32561/Camerona/blob/master/preperations/model%20training/keras/mask%20classification/training/training-resaults/training%20graph.pdf)

[Gender graph](https://github.com/benjamin32561/Camerona/blob/master/preperations/model%20training/keras/gender%20classification/training/training%20results/training%20graph.pdf)

[Beard graph](https://github.com/benjamin32561/Camerona/blob/master/preperations/model%20training/keras/beard%20classification/training/training%20results/training%20graph.pdf)

[Glass graph](https://github.com/benjamin32561/Camerona/blob/master/preperations/model%20training/keras/glass%20classification/training/after%20training/training%20graph.pdf)

### Dataset

Because we built the dataset by ourselves we needed some tools, in the [Dataset tools](https://github.com/benjamin32561/Camerona/tree/master/preperations/model%20training/dataset%20tools) you can find the tools I wrote and used during the project, I will add links to the datasets we build in the future.

### Model optimizations

After we trained the models we wanted the program to run faster, We decided to make them better by using tensorflow lite.

The optimization came out very good, you can see the performence improvement in [this excel file](https://github.com/benjamin32561/Camerona/blob/master/preperations/model%20training/program%20data.xlsx)

You can also see the difference by running the 2 different main.py codes, the tf lite is placed in tf-lite/main.py and the tensorflow is placed in keras/main.py.

## Main files

keras/main.py is using tensorflow models to make prediction, the predictions are displayed on a video window.
tf-lite/main.py is using tensorflow lite models to make prediction, the predictions are displayed on a video window.
speakers/main.py is using the tensorflow lite models to predict and use the speakers to address some one.
