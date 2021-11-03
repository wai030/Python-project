# -*- coding: utf-8 -*-
""" 
LAB 5. Question 2.
"""
#STUDENT NAME: Lam Wai Yuen
#STUDENT ID: S198249

import neurolab as nl
import numpy as np
#import pylab as pl
import matplotlib.pyplot as pl    #alternative to the above

##############
# TRAINING
##############

#reading and re-formating training data
#CHANGE THE FILE NAME BELOW

print("Loading Training Data ...")

x=np.genfromtxt('Trainingdata.csv',delimiter=',') 

x_train=x[:,0]
t_train=x[:,1]

size = len(x_train)

input = x_train.reshape(size,1)
target = t_train.reshape(size,1)

net = nl.net.newff([[-7,7]],[2,1])

# Train network
print("Training the model ...")

error = net.train(input, target, epochs=500, show=100, goal=0.02)

##############
# TESTING 
##############

print("Loading Testing Data ...")

#reading and re-formating testing data
#CHANGE THE FILE NAME BELOW
x=np.genfromtxt('Testing.csv',delimiter=',') 

x_test=x[:,0]
t_test=x[:,1]

size = len(x_test)

input_test = x_test.reshape(size,1)
target_test = t_test.reshape(size,1)

# Testing using the trained model 

print("Applying the model to the Testing Data ...")

y_test = net.sim(input_test).reshape(x_test.size)

###################
# Plotting Results 
###################

pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default SSE)')

pl.subplot(212)
pl.plot(x_test, y_test, '+',x_test , t_test, '.')
pl.legend(['Testing output', 'Target output'])
pl.show()
