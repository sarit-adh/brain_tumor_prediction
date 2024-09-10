import os
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        if image is None:
            print(f"Image {filename} could not be loaded!!")
        else:
            image = cv2.resize(image, (128, 128))
            images.append(image)
    return images

def create_dataset(positive_images_folder, negative_images_folder):
    positive_images = load_images_from_folder(positive_images_folder)
    negative_images = load_images_from_folder(negative_images_folder)

    X = np.array(positive_images + negative_images)
    y = np.array([1 for _ in range(len(positive_images))] + [0 for _ in range(len(negative_images))])
    X = X / 255.0
    y = to_categorical(y, num_classes=2)
    return X, y

def load_data(type=0, root_data_folder=None):
    '''
        type 0 : RAW
        type 1 : processed
        type 2 : external
    '''
    if type== 0 and root_data_folder is None:
        root_data_folder = "../data/raw/"


    elif type==1 and root_data_folder is None:
        root_data_folder = "../data/processed/"

    else:
        NotImplementedError("Code for loading external data not implemented")
    
    positive_images_folder = root_data_folder + "/yes/"
    negative_images_folder = root_data_folder + "/no/"

    return create_dataset(positive_images_folder, negative_images_folder)



