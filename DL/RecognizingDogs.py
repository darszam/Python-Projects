from os.path import join


image_dir = 'train/'
img_paths = [join(image_dir, filename) for filename in 
                           ['malamute.jpg',
                            'pomeranian.jpg',
                            'b.jpg'                            
                            ]]
import numpy as np
from tensorflow.python.keras.applications.resnet50 import preprocess_input
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array

img_size = 224

def read_and_prep_images(img_paths, img_height=img_size, img_width=img_size):
    imgs = [load_img(img_path, target_size=(img_height, img_width)) for img_path in img_paths]
    img_array = np.array([img_to_array(img) for img in imgs])
    return preprocess_input(img_array)

from tensorflow.python.keras.applications.resnet50 import ResNet50
my_model = ResNet50(weights='resnet50_weights_tf_dim_ordering_tf_kernels.h5')
test_data = read_and_prep_images(img_paths)
preds = my_model.predict(test_data)

from decode_predictions import decode_predictions
from Helper import visualize
most_likely_labels = decode_predictions(preds, top=3, class_list_path='imagenet_class_index.json')

visualize(img_paths, most_likely_labels)