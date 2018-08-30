import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from tensorflow.python import keras

img_rows, img_cols = 28, 28
num_classes = 10
def prep_data(raw):
    y = raw[:, 0]
    out_y = keras.utils.to_categorical(y, num_classes)
    
    x = raw[:,1:]
    num_images = raw.shape[0]
    out_x = x.reshape(num_images, img_rows, img_cols, 1)
    out_x = out_x / 255
    return out_x, out_y
def prep_test_data(raw):
    x = raw[:,:]
    num_images = raw.shape[0]
    out_x = x.reshape(num_images, img_rows, img_cols, 1)
    out_x = out_x / 255
    return out_x
digits_file = "../input/train.csv"
digits_data = np.loadtxt(digits_file, skiprows=1, delimiter=',')
x, y = prep_data(digits_data)

digits_test_data = np.loadtxt("../input/test.csv",skiprows = 1, delimiter=',')
digits_test_data_X = prep_test_data(digits_test_data)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D

digits_model = Sequential()
digits_model.add(Conv2D(12, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(img_rows, img_cols, 1)))
digits_model.add(Conv2D(12, kernel_size=(3, 3), activation='relu'))
digits_model.add(Conv2D(12, kernel_size=(3, 3), activation='relu'))
digits_model.add(Flatten())
digits_model.add(Dense(100, activation='relu'))
digits_model.add(Dense(num_classes, activation='softmax'))

digits_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])
digits_model.fit(x, y,
          batch_size=100,
          epochs=30,
          validation_split = 0.2)
          

predictions = digits_model.predict(digits_test_data_X)
predictions = np.argmax(predictions,axis = 1)
submission = pd.DataFrame({'ImageId': range(1,28001), 'Label': predictions})
submission.to_csv('submission3.csv', index=False)
print("Finished")
