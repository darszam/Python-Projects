from PIL import ImageShow, Image
import numpy as np
import matplotlib.pyplot as plt

def visualize(images_paths,most_likely_labels):
    for i, img_path in enumerate(images_paths):
        img = Image.open(img_path)
        img_arr = np.asarray(img)
        plt.imshow(img_arr)
        plt.axis('off')
        print(most_likely_labels[i])
        plt.show()
