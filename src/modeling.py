
from src.preprocessing import get_preprocessed_data
from tensorflow.keras.applications import VGG16, VGG19, ResNet50
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import cv2
import os

class Model(object):
    
    def __init__(self, model_type, epochs):
        self.model_type = model_type
        self.epochs = epochs
        self.trained_model = None
    
    def create_model(self, train_aug, X_val, y_val):
        
        if self.trained_model:
            return self.trained_model
        
        
        if self.model_type== "vgg16":
            # Building a base model using Transfer Learning (VGG16)
            base_model = VGG16(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
            base_model.trainable = False
        
        elif self.model_type== "vgg19":
            # Building a base model using Transfer Learning (VGG19)
            base_model = VGG19(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
            base_model.trainable = False
            
        elif self.model_type== "resnet":
            # Building a base model using Transfer Learning (resnet50)
            base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
            base_model.trainable = False
        
        else:
            print("{self.model_type} yet not supported")
        
            

        model = Sequential()
        model.add(base_model)
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(2, activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Train the model
        model.fit(train_aug, epochs=self.epochs, validation_data=(X_val, y_val))
        
        self.trained_model =  model
    
    def persist_model(self, directory):
        
        if not self.trained_model:
            print("Model not trained!!")
        
        file_path = os.path.join(directory, f"{self.model_type}_{self.epochs}.keras" )
        self.trained_model.save(file_path)
        
    def load_model(self, directory):
        
        try:
            file_path = os.path.join(directory, f"{self.model_type}_{self.epochs}.keras" )
            self.trained_model = load_model(file_path)
            
        except FileNotFoundError:
            # File does not exist
            print(f"Error: Model file doesn't exist in {file_path}")
            
        except Exception as e:
            # General exception
            print(f"Error loading the model {str(e)}")
            
    def predict(self, image_path):
        
        image = cv2.imread(image_path)
        if image is None:
            print(f"Image {image_path} could not be loaded!!")
        else:
            image = cv2.resize(image, (128, 128))
        
        X = np.array([image])
        X = X / 255.0
        y_pred = self.trained_model.predict(X)
        return y_pred
        
        

    def evaluate_model(self, X_test, y_test):
        
        if not self.trained_model:
            print("Model not trained!!")
        
        # Get prediction
        y_pred = self.trained_model.predict(X_test)
        y_pred_classes = np.argmax(y_pred, axis=1)
        y_true = np.argmax(y_test, axis=1)
        
        
        
        # Classification report and confusion matrix
        print("Classification Report:\n", classification_report(y_true, y_pred_classes))
        print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred_classes))
        
        classification_report_dict = classification_report(y_true, y_pred_classes, output_dict=True)
        return classification_report_dict
        
        