# packages
# pip install NeuroLab
#     or
# conda install -c labfabulous neurolab
#

#
# This program train a single perceptron to simulate a "and" function
# s198249 Lam Wai Yuen

import neurolab as nl
import matplotlib.pyplot as pl

##AND
#input = [[0, 0], [0, 1], [1, 0], [1, 1]]
#target = [[0],   [0],   [0],     [1]]

##OR
input = [[0, 0], [0, 1], [1, 0], [1, 1]]
target = [[0],   [1],   [1],     [1]]
##XOR
#input = [[0, 0], [0, 1], [1, 0], [1, 1]]
#target = [[0],   [1],   [1],     [0]]
#
#  Create a single layer perceptron
#

net = nl.net.newp([[0, 1],[0, 1]], 1)

#
#  Training
#

error_progress = net.train(input, target, epochs=100, show=10, lr=0.1)


#
#  Testing
#

y = net.sim(input)

#
#  Plot the result
#

pl.subplot(211)  # a subfigure

pl.plot(error_progress)
pl.xlabel('Number of epochs')
pl.ylabel('Training error')

pl.subplot(212)  # a subfigure
pl.plot(target, '+',  y, 'x')
pl.xlabel('Test case')
pl.ylabel('Output)')
pl.legend(['Target output', 'System output'])


pl.show()
