
# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
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


while not end:

    try:
        file=input("enter a picture's file name (or exit to end):")
        if file != "exit":            
            # load the image
            img = load_image(file)           
            # predict the class
            result = model.predict(img)
            # check result
            if result > 0.5:
                print(result, " Dog!")
            else:
                print(result, " Cat!")
        else:
            end =True
    except OSError as e:
        print("Cannot Open File")
    
    
        
    

