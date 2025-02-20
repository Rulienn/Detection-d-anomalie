import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#keras
import keras
from keras.models import Model
from keras.layers import Input, add
from keras.layers import Layer, Dense, Dropout, Activation, Flatten, Reshape
from keras import regularizers
from keras.regularizers import l2
from keras.layers.convolutional import Conv2D, MaxPooling2D, UpSampling2D, ZeroPadding2D
from keras.utils import np_utils


def load_images_from_folder(folder_path, target_size=None):
    images = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, filename)
            image = Image.open(img_path)
            if target_size:
                image = image.resize(target_size)  # Redimensionner l'image si nécessaire
            image_array = np.array(image)  # Convertir l'image en tableau NumPy
            images.append(image_array)
            filenames.append(filename)
    return np.array(images), filenames

def normalize(images):
    s=images.shape
    images = images.astype("float32")/255
    images = images.reshape(s[0],s[1]*s[2]*s[3])
    return images

folder_path = '/home/jgayraud/Documents/MIC3/BE/engine_wiring/test/blue_hoop'
target_size = (400, 400)  
images, filenames = load_images_from_folder(folder_path, target_size)
images = normalize(images)


# Afficher la forme des images chargées
print(f"Forme des images chargées : {images.shape}")
#plt.imshow(images[4,:,:,:])
#plt.axis('off')  # Masquer les axes
#plt.show()