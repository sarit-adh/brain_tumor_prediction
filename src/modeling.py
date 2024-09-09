
from preprocessing import get_preprocessed_data
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def create_model(train_aug, X_val, y_val):
    
    
    # Building a model using Transfer Learning (VGG16)
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
    base_model.trainable = False

    model = Sequential()
    model.add(base_model)
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_aug, epochs=10, validation_data=(X_val, y_val))
    
    return model


def evaluate_model(model, X_test, y_test):
    
    # Get prediction
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test, axis=1)
    
    # Classification report and confusion matrix
    print("Classification Report:\n", classification_report(y_true, y_pred_classes))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred_classes))
    
def main():
    train_aug, X_test, y_test = get_preprocessed_data()
    
    model = create_model(train_aug, X_test, y_test)
    evaluate_model(model, X_test, y_test)
    
    
if __name__=="__main__":
    main()