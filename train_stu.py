# -*- coding: utf-8 -*-
"""
Student ID:s198249
Name:Lam Wai Yuen
"""

# save the final model to file
import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
# define cnn model

def define_model():
	# load model
	model = VGG16(include_top=False, input_shape=(224, 224, 3))
	# mark loaded layers as not trainable
	for layer in model.layers:
		layer.trainable = False
	# add new classifier layers
	flat1 = Flatten()(model.layers[-1].output)
	class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
	output = Dense(1, activation='sigmoid')(class1)
	# define new model
	model = Model(inputs=model.inputs, outputs=output)
	# compile model 
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model

# Training.

def train():
    # define model
	model = define_model()
	# create data generator
	datagen = ImageDataGenerator(featurewise_center=True)
	# specify imagenet mean values for centering
	datagen.mean = [123.68, 116.779, 103.939]
	# prepare training data
	
	train_data = datagen.flow_from_directory('dogs_vs_cats/train',
		class_mode='binary', batch_size=10, target_size=(224, 224))
	solve_cudnn_error()
	# fit model
	model.fit(train_data, steps_per_epoch=len(train_data), epochs=5, verbose=1)
	# save model
	
	model.save('s198249_Model.h5')


##solve_cudnn_error()
# entry point, run the test harness
train()

