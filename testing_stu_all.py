import os

# make a prediction for a new image.
import tensorflow as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import os
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
# define cnn model

# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img



# entry point, run the example
end = False

# load model

model = load_model('s198249_model.h5')


correct=0;
wrong=0;
count=0;

basedir = 'dogs_vs_cats/test/cats'

for file in os.listdir(basedir):
    count+=1;
    img = load_image(os.path.join(basedir, file))   
    # predict the class
    result = model.predict(img)
    # check result
    if result > 0.5:
        wrong+=1
    else:
        correct+=1
    if (count % 10 == 0):
        print("Cats: Images {} Correct {} Wrong {}".format(count, correct, wrong))

basedir = 'dogs_vs_cats/test/dogs'

correct=0;
wrong=0;
count=0;

for file in os.listdir(basedir):
    count+=1;
    img = load_image(os.path.join(basedir, file))   
    # predict the class
    result = model.predict(img)
    # check result
    if result <= 0.5:
        wrong+=1
    else:
        correct+=1
    if (count % 10 == 0):
        print("Dogs: Images {} Correct {} Wrong {}".format(count, correct, wrong))
        
